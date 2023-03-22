from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ChatRoom, Message

def chatroom_list(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chatroom_list.html', {'chatrooms': chatrooms})

def chatroom_detail(request, chatroom_id):
    chatroom = ChatRoom.objects.get(pk=chatroom_id)
    messages = Message.objects.filter(chatroom=chatroom).order_by('timestamp')
    return render(request, 'chatroom_detail.html', {'chatroom': chatroom, 'messages': messages})
