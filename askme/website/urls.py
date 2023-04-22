from django.urls import path

from .views import *


urlpatterns = [
    path('',listing, name='main'),
    path('login/', Login, name='login'),
    path('signup/',registration,name='signup'),
    path('hot/',hot,name='hots'),
    path('ask/',ask,name='ask'),
    path('question/<int:id>/', questions, name='questions'),
    path('tag/<slug:tg>/',tag_search,name='tag'),
    path('logout/',logout,name='logout'),
    path('edit/',settings,name='edit')
    
]