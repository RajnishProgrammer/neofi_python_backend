from django.urls import path
from users.views import UserSignUp, UserLogin, NoteCreate, NoteDetail, NoteShare, NoteUpdate, NoteVersionHistory, NoteDelete

urlpatterns = [
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('notes/create/', NoteCreate.as_view(), name='note_create'),
    path('notes/<int:id>/', NoteDetail.as_view(), name='note_detail'),
    path('notes/share/', NoteShare.as_view(), name='note_share'),
    path('notes/update/<int:id>/', NoteUpdate.as_view(), name='note_update'),
    path('notes/version-history/<int:id>/', NoteVersionHistory.as_view(), name='note_version_history'),
    path('notes/<int:id>/delete/', NoteDelete.as_view(), name='note_delete'),
]
