from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    rating = models.IntegerField()
    tag = models.ManyToManyField('tag',related_name='tgs')
    publicationMoment = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'


class tag(models.Model):
    tag = models.CharField(max_length=20)
    relev = models.IntegerField()


    def __str__(self):
        return f'{self.tag}'


class answer(models.Model):
    authorId = models.ForeignKey('user',on_delete=models.PROTECT)
    txt = models.TextField(max_length=500)
    questionId = models.ForeignKey('question',on_delete=models.PROTECT)
    rating = models.IntegerField()
    isRight = models.BooleanField()


    def __str__(self):
        return f'{self.id}'


class user(models.Model):
    profile = models.OneToOneField(User,on_delete=models.PROTECT)
    username = models.CharField(max_length=100)
    avatar = models.ImageField(null=True,blank=True)

    def __str__(self):
        return f'{self.username}'

QUESTIONS = []
ANSWERS = []


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

    ANSWERS.append({
        'user': 'user'+str(i),
        'id': i,
        'text': 'text'+str(i),
    })


