from django.urls import path
from django.contrib import admin
from home import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('addFace/', views.addFace),
    path('welcome/<int:face_id>/', views.welcome),
]
