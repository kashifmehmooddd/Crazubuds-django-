from django.shortcuts import render
from django.http import HttpResponse

rooms = [
  {'id': 1, 'name': "kashif"},
  {'id': 2, 'name': "Abdullah"},
  {'id': 3, 'name': "Umer"},

]

def home(request):
  return render(request, 'base/home.html', {'rooms': rooms})

def room(request, id):
  room = None
  for i in rooms:
    if i['id'] == int(id):
      room = i
      break
  return render(request, 'base/room.html', {'room': room})
