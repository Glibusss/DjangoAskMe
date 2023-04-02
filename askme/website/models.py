from django.db import models

# Create your models here.
QUESTIONS = []
answers = []


for i in range(1,30):

    QUESTIONS.append({
        'id': i,
        'title': 'title'+str(i),
        'text': 'text'+str(i),
        'tags':'tag'+str(i),
    })

    
QUESTIONS.append({
        'id': len(QUESTIONS),
        'title': 'qqqq',
        'text': 'tttt',
        'tags':'tag1',
    })


for i in range(1,30):

    answers.append({
        'user': 'user'+str(i),
        'id': i,
        'text': 'text'+str(i),
    })