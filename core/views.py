from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import Room, Message

def index(request):
    rooms =  Room.objects.all()

    return render(request, 'chat.html', {"rooms":rooms})

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'messages': Message.objects.filter(room=Room.objects.get(name=room_name))
    })