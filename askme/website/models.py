from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce


# Create your models here.

class questionVote(models.Model):
    question = models.ForeignKey('question',on_delete=models.CASCADE)
    user = models.ForeignKey('Profile',on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(1,'like'),(-1,'dislike')],default=1)


class answerVote(models.Model):
    answer = models.ForeignKey('answer',on_delete=models.CASCADE)
    user = models.ForeignKey('Profile',on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(1,'like'),(-1,'dislike')],default=1)
    
class questionManager(models.Manager):


    def orderByRating(self):
        return self.alias(rat=Sum('questionvote__score')).order_by('-rat','-publicationMoment')
    

    def orderByDate(self):
        return self.alias(rat=Sum('questionvote__score')).order_by('-publicationMoment','-rat')
    

    def findId(self,id):
        try:
            q=self.get(pk=id)
        except question.DoesNotExist:
            return None
        return q
    

    def filterTagByDate(self,tg):
        return self.filter(tag__tag=tg).alias(rat=Sum('questionvote__score')).order_by('-publicationMoment','-rat')
    

    def getLast(self):
        if self.all().last()==None:
            return 0
        else:
            return self.all().last().id 
    

    

class question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    tag = models.ManyToManyField('tag',blank=True,null=True)
    publicationMoment = models.DateTimeField(auto_now=True)
    authorId = models.ForeignKey('Profile',on_delete=models.PROTECT,default = 1)
    objects=questionManager()


    
    def __str__(self):
        return f'{self.title}'


class tagManager(models.Manager):
     

     def findTag(self,tg):
         try:
             self.get(tag=tg)
         except tag.DoesNotExist:
             return False
         return True
     
     def getLastId(self):
        if self.all().last()==None:
            return 0
        else:
            return self.all().last().id 

class tag(models.Model):
    tag = models.CharField(max_length=20)
    objects = tagManager()


    def __str__(self):
        return f'{self.tag}'
    

class answerManager(models.Manager):

    def getLastId(self):
        if self.all().last()==None:
            return 0
        else:
            return self.all().last().id 
    
    def sortByTop(self,id):
        
        return self.alias(rat=Coalesce(Sum('answervote__score'),0)).filter(questionId = id).order_by('-isRight','-rat',)
        

class answer(models.Model):
    authorId = models.ForeignKey('Profile',on_delete=models.PROTECT)
    txt = models.TextField(max_length=500)
    questionId = models.ForeignKey('question',on_delete=models.PROTECT)
    isRight = models.BooleanField(default=False)
    objects = answerManager()

    def __str__(self):
        return f'{self.id}'

class userManager(models.Manager):


    def getLastId(self):
        if self.all().last()==None:
            return 0
        else:
            return self.all().last().id 
        
    

class Profile(models.Model):
    profile = models.OneToOneField(User,on_delete=models.PROTECT)
    nickname = models.CharField(max_length=100,default='')
    avatar = models.ImageField(null=True,blank=True)
    objects = userManager()

    def __str__(self):
        return f'{self.nickname}'
    











    

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


