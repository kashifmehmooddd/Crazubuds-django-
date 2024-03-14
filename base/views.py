from django.shortcuts import render
from .models import Room

def home(request):
  return render(request, 'base/home.html', {'rooms': Room.objects.all()})

def room(request, id):
  room = Room.objects.get(pk=id)
  return render(request, 'base/room.html', {'room': room})
