from django.urls import path

from .views import *

urlpatterns = [
    path('',listing, name = 'main'),
    path('login/', login, name='login'),
    path('signup/',registration,name='signup'),
    path('hot/',hot,name='hots'),
    path('ask/',ask,name='ask'),
    path('question/<int:id>/', question, name='question'),
    path('tag/<slug:tg>/',tag,name='tag'),
    path('404/',pageNotFound,name = '404' ),
]