from django.urls import path

from .views import *


urlpatterns = [
    path('',listing, name='main'),
    path('login/', login, name='login'),
    path('signup/',registration,name='signup'),
    path('hot/',hot,name='hots'),
    path('ask/',ask,name='ask'),
    path('questions/<int:id>/', questions, name='questions'),
    path('tag/<slug:tg>/',tag,name='tag'),
    
]