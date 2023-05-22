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
    path('edit/',settings,name='edit'),
    path('upvote_q/',upvote_question,name='voteupq'),
    path('downvote_q/',downvote_question,name='votedownq'),
    path('upvote_a/',upvote_answer,name='voteupa'),
    path('downvote_a/',downvote_answer,name='votedowna'),
    path('correct/',make_correct,name='correct'),
    
]