from django.contrib import admin
from .models import User, Note, NoteVersion

# Register your models here.
admin.site.register(User)
admin.site.register(Note)
admin.site.register(NoteVersion)