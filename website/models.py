from django.db import models

# Create your models here.
questions = []
answers = []


for i in range(1,30):

    questions.append({
        'id': i+4,
        'title': 'title'+str(i),
        'text': 'text'+str(i),
        'tags':'tag'+str(i),
    })

    
questions.append({
        'id': len(questions),
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