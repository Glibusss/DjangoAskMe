import random
from django.core.management.base import BaseCommand, CommandError
from website.models import question, answer,user,tag,answerVote,questionVote
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'fill_db [number]'



    def add_arguments(self, parser):
        return parser.add_argument('ratio',nargs='+',type=int)
    

    def handle(self, *args, **options):
       ratio = int(options['ratio'][0])
       edgeUser = user.objects.getLastId()
       edgeQ=question.objects.getLast()
       edgeAns = answer.objects.getLastId()
       edgeTag = tag.objects.getLastId()
           
       listTags = []
       listUsers = []
       listQuestions=[]
       listAns = []
       for i in range (0,ratio):
           tg =tag(tag='Tag'+str(edgeTag+i))
           tg.save()
           listTags.append(
               tg
           )
        
       for i in range (0,ratio):
           p=User(username = 'user'+str(i+edgeUser+1), password = '1111')
           p.save()
           u = user(profile=p, username='USER'+str(i+edgeUser+1))
           u.save()
           listUsers.append(
               u
           )


       for i in range (0,ratio*10):
           q = question(title='Title'+str(i+edgeQ+1), description = 'Desc'+str(i+edgeQ+1), authorId = listUsers[random.randint(0,ratio-1)])
           q.save()
           temp =listTags[random.randint(0,ratio-1)]
           q.tag.add(temp)
           listQuestions.append(
               q
           )

       for i in range (0,ratio*100):
           a = answer(authorId = listUsers[random.randint(0,ratio-1)],txt = 'ANSWER'+str(i+edgeAns+1),questionId = listQuestions[random.randint(0,ratio*10-1)],isRight =False)
           a.save()
           listAns.append(
               a
           )


       for i in range (0,ratio*100):
           lordis=random.randint(0,1)
           if lordis==1:
                 like=questionVote(question=listQuestions[random.randint(0,ratio*10-1)],user = listUsers[random.randint(0,ratio-1)],score=1)
                 like.save()
           else:
                 dislike=questionVote(question=listQuestions[random.randint(0,ratio*10-1)],user=listUsers[random.randint(0,ratio-1)],score=-1)
                 dislike.save()


       for i in range (0,ratio*100):
           lordis=random.randint(0,1)
           if lordis==1:
               like=answerVote(answer=listAns[random.randint(0,ratio*100-1)],user = listUsers[random.randint(0,ratio-1)],score=1)
               like.save()
           else:
               dislike=answerVote(answer=listAns[random.randint(0,ratio*100-1)],user=listUsers[random.randint(0,ratio-1)],score=-1)
               dislike.save()