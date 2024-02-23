from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Note, NoteVersion
from .serializers import NoteSerializer, NoteVersionSerializer
from django.contrib.auth import get_user_model


user = get_user_model()

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = user.objects.create_user(username='test_user1', password='test_password1')
        self.client.force_authenticate(user=self.user)
        self.note_data = {'owner': self.user.id, 'content': 'Test note content'}
        print('setup is done!')

    def test_create_note(self):
        response = self.client.post(reverse('note_create'), self.note_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print('create-note api testing is done !')

    def test_get_note_detail(self):
        note = Note.objects.create(owner=self.user, content='Test note content')
        print('note', note)
        response = self.client.get(reverse('note_detail', kwargs={'id': note.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('response', response)
        self.assertEqual(response.data['content'], 'Test note content')
        print('note-detail api testing is done !')

    def test_share_note(self):
        note = Note.objects.create(owner=self.user, content='Test note content')
        other_user = user.objects.create_user(username='other_user1', password='other_password1', email='other@user1.com')
        data = {'note_id': note.id, 'users': [other_user.username]}
        response = self.client.post(reverse('note_share'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('share-note api testing is done !')

    def test_update_note(self):
        note = Note.objects.create(owner=self.user, content='Initial content')
        data = {'content': 'Updated content'}
        response = self.client.put(reverse('note_update', kwargs={'id': note.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('note-update api testing is done !')

    def test_get_note_version_history(self):
        note = Note.objects.create(owner=self.user, content='Test note content')
        note_version = NoteVersion.objects.create(note=note, user=self.user, changes='Changed content')
        response = self.client.get(reverse('note_version_history', kwargs={'id': note.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        print('version-history api testing is done !')

    def test_delete_note(self):
        note = Note.objects.create(owner=self.user, content='Test note content')
        response = self.client.delete(reverse('note_delete', kwargs={'id': note.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print('delete api testing is done !')

    def test_user_login(self):
        user = {'username_or_email': self.user.username, 'password': 'test_password1'}
        print(self.user.username, self.user.password)
        response = self.client.post(reverse('login'), user, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('login api testing is done !')

    def test_user_registration(self):
        new_user = {'username': 'new_user', 'email': 'new_user@example.com', 'password': 'new_password'}
        response = self.client.post(reverse('signup'), new_user, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print('registration api testing is done !')
