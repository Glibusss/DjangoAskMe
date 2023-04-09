from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count,F


# Create your models here.


class upvoteQuestion(models.Model):
    question = models.ForeignKey('question',on_delete=models.CASCADE)
    user = models.ForeignKey('user',on_delete=models.CASCADE)


class upvoteAnswer(models.Model):
    answer = models.ForeignKey('answer',on_delete=models.CASCADE)
    user = models.ForeignKey('user',on_delete=models.CASCADE)


class downvoteQuestion(models.Model):
    question = models.ForeignKey('question',on_delete=models.CASCADE)
    user = models.ForeignKey('user',on_delete=models.CASCADE)



class downvoteAnswer(models.Model):
    answer = models.ForeignKey('answer',on_delete=models.CASCADE)
    user = models.ForeignKey('user',on_delete=models.CASCADE)

    
class questionManager(models.Manager):


    def orderByRating(self):
        return self.annotate(
            likes = Count('upvotequestion',distinct=True), dis = Count('downvotequestion',distinct=True)).annotate(rat=(F('likes')-F('dis'))).order_by('-rat')
    

    def orderByDate(self):
        return self.annotate(rat = Count('upvotequestion')-Count('downvotequestion')).order_by('-publicationMoment','-rat')
    

    def findId(self,id):
        try:
            q=self.get(pk=id)
        except question.DoesNotExist:
            return None
        return q
    

    def filterTagByDate(self,tg):
        return self.filter(tag__tag=tg).annotate(rat = Count('upvotequestion')-Count('downvotequestion')).order_by('-publicationMoment','-rat')
    

class question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    tag = models.ManyToManyField('tag',related_name='tgs')
    publicationMoment = models.DateTimeField(auto_now=True)
    authorId = models.ForeignKey('user',on_delete=models.PROTECT,default = 1)
    objects=questionManager()
    

    def __str__(self):
        return f'{self.title}'


class tag(models.Model):
    tag = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.tag}'

class answerManager(models.Manager):


    def sortByTop(self,id):
        return self.filter(questionId = id).annotate(
            likes = Count('upvoteanswer',distinct=True), dis = Count('downvoteanswer',distinct=True)).annotate(rat=(F('likes')-F('dis'))).order_by('-rat')
        

class answer(models.Model):
    authorId = models.ForeignKey('user',on_delete=models.PROTECT)
    txt = models.TextField(max_length=500)
    questionId = models.ForeignKey('question',on_delete=models.PROTECT)
    isRight = models.BooleanField()
    objects = answerManager()

    def __str__(self):
        return f'{self.id}'

class userManager(models.Manager):


    def getLastId(self):
        return self.all().last().id
    

class user(models.Model):
    profile = models.OneToOneField(User,on_delete=models.PROTECT)
    username = models.CharField(max_length=100)
    avatar = models.ImageField(null=True,blank=True)
    objects = userManager()
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


