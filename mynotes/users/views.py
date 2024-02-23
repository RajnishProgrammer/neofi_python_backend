from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserLoginSerializer, NoteSerializer, NoteVersionSerializer
from .models import Note, User, NoteVersion
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils import timezone


class UserSignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username_or_email = serializer.validated_data['username_or_email']
            password = serializer.validated_data['password']

            # Authenticate user
            user = authenticate(username=username_or_email, password=password)
            if user:
                # Generate or retrieve authentication token
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class NoteCreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.data['owner'] = request.user.id
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)  # Assign current user as owner
            return Response({'message': 'Note created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            # Retrieve the note by its ID
            note = Note.objects.get(id=id)
            
            # Check if the authenticated user is the owner or a shared user of the note
            if request.user == note.owner or request.user in note.shared_users.all():
                # Serialize the note data
                serializer = NoteSerializer(note)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'You do not have permission to view this note'}, status=status.HTTP_403_FORBIDDEN)
        except Note.DoesNotExist:
            return Response({'error': 'Note does not exist'}, status=status.HTTP_404_NOT_FOUND)


class NoteShare(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check if the request data contains the necessary fields
        if 'note_id' not in request.data or 'users' not in request.data:
            return Response({'error': 'Note ID and users list are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve the note by its ID
        try:
            note = Note.objects.get(id=request.data['note_id'])
        except Note.DoesNotExist:
            return Response({'error': 'Note does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the authenticated user is the owner of the note
        if request.user != note.owner:
            return Response({'error': 'You do not have permission to share this note'}, status=status.HTTP_403_FORBIDDEN)
        
        # Add the specified users to the list of shared users for the note
        for username in request.data['users']:
            try:
                user = User.objects.get(username=username)
                note.shared_users.add(user)
            except User.DoesNotExist:
                pass  # Ignore invalid usernames
        
        # Save the changes to the note
        note.save()
        
        return Response({'message': 'Note shared successfully'}, status=status.HTTP_200_OK)
    

class NoteUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        # Check if the request data contains the necessary fields
        if 'content' not in request.data:
            return Response({'error': 'Content is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Retrieve the note by its ID
        try:
            note = Note.objects.get(id=id)
        except Note.DoesNotExist:
            return Response({'error': 'Note does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if the authenticated user is the owner or a shared user of the note
        if request.user != note.owner and request.user not in note.shared_users.all():
            return Response({'error': 'You do not have permission to edit this note'}, status=status.HTTP_403_FORBIDDEN)
        
        new_content = request.data.get('content', '')
        if new_content:
            # Update the content of the note
            note.content += "\n" + request.data['content']  # Append the new content to the existing content
            note.updated_at = timezone.now()  # Update the timestamp
            note.save()

            # Update NoteVersion Model
            NoteVersion.objects.create(
                note = note, 
                created_at = note.created_at,
                user = request.user,
                changes = new_content
            )
            
            return Response({'message': 'Note updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Content is required'}, status=status.HTTP_400_BAD_REQUEST)
    

class NoteVersionHistory(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        print('id:', id)
        try:
            note = Note.objects.get(id=id)

            if request.user == note.owner or request.user in note.shared_users.all():
                note_versions = NoteVersion.objects.filter(note_id=id)
                print("note version:", note_versions)
                if not note_versions:
                    return Response({'error': 'Note version history not found'}, status=status.HTTP_404_NOT_FOUND)
                
                # Serialize the version history data
                serializer = NoteVersionSerializer(note_versions, many=True)
                print("serializer data: ", serializer.data)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'You do not have permission to view the version history of this note'}, status=status.HTTP_403_FORBIDDEN)
        except NoteVersion.DoesNotExist:
            return Response({'error': 'Note version history not found'}, status=status.HTTP_404_NOT_FOUND)
        

class NoteDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            # Retrieve the note by its ID
            note = Note.objects.get(id=id)
            print("note:",note)
            # Check if the authenticated user is the owner of the note
            if request.user == note.owner:
                # Delete the note
                note.delete()
                return Response({'message': 'Note deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'You do not have permission to delete this note'}, status=status.HTTP_403_FORBIDDEN)
        except Note.DoesNotExist:
            return Response({'error': 'Note does not exist'}, status=status.HTTP_404_NOT_FOUND)