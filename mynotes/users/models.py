from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    shared_users = models.ManyToManyField(User, related_name='shared_notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Add any other fields as needed

    def __str__(self):
        return self.content

class NoteVersion(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    changes = models.TextField()

    def __str__(self):
        return f"Note: {self.note}, Timestamp: {self.timestamp}, User: {self.user}"