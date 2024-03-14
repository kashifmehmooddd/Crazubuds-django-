from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

def home(request):
  return render(request, 'base/home.html', {'rooms': Room.objects.all()})

def room(request, id):
  room = Room.objects.get(pk=id)
  return render(request, 'base/room.html', {'room': room})

def createRoom(request):
  form = RoomForm()
  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('home')

  context={ "form": form }
  return render(request, 'base/room_form.html', context)
