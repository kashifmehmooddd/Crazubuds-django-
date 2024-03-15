from django.urls import path
from . import views

urlpatterns = [
  path('login', views.loginPage, name="login"),
  path("/logut", views.logoutUser, name="logout"),
  path('', views.home, name="home"),
  path('room/<str:id>', views.room, name="room"),
  path('create-room', views.createRoom, name="createRoom"),
  path('update-room/<int:pk>', views.updateRoom, name="updateRoom"),
  path('delete-room/<int:pk>', views.deleteRoom, name="deleteRoom"),
]

