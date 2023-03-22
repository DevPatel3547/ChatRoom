from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=255)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
