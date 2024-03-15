from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Room, Topic
from .forms import RoomForm

def loginPage(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
      user = User.objects.get(username=username)
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
      else:
        messages.error(request, "username or password is invalid!")
    except:
      messages.error(request, "User doesn't Exists!")


  return render(request, 'base/login_register.html')

def logoutUser(request):
  logout(request)
  return redirect('home')

def home(request):
  q=request.GET.get('q') if request.GET.get('q') != None else ''
  return render(request, 'base/home.html', {'rooms': Room.objects.filter(
    Q(topic__name__icontains=q) |
    Q(name__icontains=q)), 'topics': Topic.objects.all()})

def room(request, id):
  room = Room.objects.get(pk=id)
  return render(request, 'base/room.html', {'room': room})

@login_required(login_url='/login')
def createRoom(request):
  form = RoomForm()
  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('home')

  context={ "form": form }
  return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
  room = Room.objects.get(pk=pk)
  form = RoomForm(instance=room)
  if request.method == 'POST':
    form = RoomForm(request.POST, instance=room)
    if form.is_valid:
      form.save()
      return redirect('home')

  context={ "form": form }
  return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
  room = Room.objects.get(pk=pk)
  if request.method == 'POST':
    room.delete()
    return redirect('home')
  context={ "obj": room }
  return render(request, 'base/delete.html', context)
