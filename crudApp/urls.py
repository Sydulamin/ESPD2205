from django.urls import path

from .views import *

urlpatterns = [

    path('', BASE, name='base'),
    path('Create/', Create, name='Create'),
    path('profile/<int:id>/', profile, name='profile'),
    path('login/', login, name='login'),
    path('reg/', registration, name='reg'),
    path('DeleteProfile/<int:id>/', DeleteProfile, name='DeleteProfile'),
    path('update/<id>/', update, name='updateProfile'),


]
