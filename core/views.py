from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
import json
from .models import Room, Message

def index(request):
    rooms =  Room.objects.all()
    return render(request, 'chat.html', {"rooms":rooms})

def room(request, room_name):
    print(room_name,"*"*50)
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'messages': Message.objects.filter(room=Room.objects.get(name=room_name))
    })

@csrf_exempt
def addroom(request):
    print("Add Room Called", request.POST)
    try:
        roomname = request.POST['roomname']
        roomlabel = request.POST['roomlabel']
        print(Room.objects.filter(name=roomname).count())
        if(Room.objects.filter(name=roomname).count() > 0):
            raise Exception("Duplicate Room")
        newroom = Room.objects.create(name=roomname, label=roomlabel)
        
        return JsonResponse({
            "name": newroom.name,
            "label": newroom.label
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            "error": str(e)
        }, status=400)