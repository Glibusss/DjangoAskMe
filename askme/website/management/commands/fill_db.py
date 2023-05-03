import random
from django.core.management.base import BaseCommand
from website.models import Question, Answer,Profile,Tag,AnswerVote,QuestionVote
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'fill_db [number]'



    def add_arguments(self, parser):
        return parser.add_argument('ratio',nargs='+',type=int)
    

    def handle(self, *args, **options):
       ratio = int(options['ratio'][0])
       edgeUser = User.objects.getLastId()
       edgeQ=Question.objects.getLast()
       edgeAns = Answer.objects.getLastId()
       edgeTag = Tag.objects.getLastId()
           
       listTags = []
       listUsers = []
       listQuestions=[]
       listAns = []
       for i in range (0,ratio):
           tg =Tag(tag='Tag'+str(edgeTag+i))
           tg.save()
           listTags.append(
               tg
           )
        
       for i in range (0,ratio):
           p=User(username = 'user'+str(i+edgeUser+1), password = '1111')
           p.save()
           u = Profile(profile=p, nickname='USER'+str(i+edgeUser+1))
           u.save()
           listUsers.append(
               u
           )


       for i in range (0,ratio*10):
           q = Question(title='Title'+str(i+edgeQ+1), description = 'Desc'+str(i+edgeQ+1), authorId = listUsers[random.randint(0,ratio-1)])
           q.save()
           temp =listTags[random.randint(0,ratio-1)]
           q.tag.add(temp)
           listQuestions.append(
               q
           )

       for i in range (0,ratio*100):
           a = Answer(authorId = listUsers[random.randint(0,ratio-1)],txt = 'ANSWER'+str(i+edgeAns+1),questionId = listQuestions[random.randint(0,ratio*10-1)],isRight =False)
           a.save()
           listAns.append(
               a
           )


       for i in range (0,ratio*100):
           lordis=random.randint(0,1)
           if lordis==1:
                 like=QuestionVote(question=listQuestions[random.randint(0,ratio*10-1)],user = listUsers[random.randint(0,ratio-1)],score=1)
                 like.save()
           else:
                 dislike=QuestionVote(question=listQuestions[random.randint(0,ratio*10-1)],user=listUsers[random.randint(0,ratio-1)],score=-1)
                 dislike.save()


       for i in range (0,ratio*100):
           lordis=random.randint(0,1)
           if lordis==1:
               like=AnswerVote(answer=listAns[random.randint(0,ratio*100-1)],user = listUsers[random.randint(0,ratio-1)],score=1)
               like.save()
           else:
               dislike=AnswerVote(answer=listAns[random.randint(0,ratio*100-1)],user=listUsers[random.randint(0,ratio-1)],score=-1)
               dislike.save()