from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator
from website.models import ANSWERS, QUESTIONS, question,answer,user


qq = question.objects.order_by('-publicationMoment')



def paginate(obj_list, request, per_page=1):

    paginator=Paginator(obj_list,per_page)

    page_number = request.GET.get('page')

    page_obj=paginator.get_page(page_number)
    
    return page_obj
   

# Create your views here.


def listing(request):
    return render(request,'listing.html',{'page_obj':paginate(qq,request,4),'pagename':'New Questions','linkname':'Hot questions','link':'hots'})
    
    
def login(request):
    return render(request,'login_form.html')


def registration(request):
    return render(request, 'reg_form.html')


def hot(request):
    qr = question.objects.order_by('-rating','-publicationMoment')
    return render(request,'listing.html',{'page_obj':paginate(qr,request,4),'questions':qr,'pagename':'Hot questions','linkname':'New Questions','link':'main'})
    
    

def ask(request):                                     
    return render(request,'question_form_login.html')


def questions(request,id):
   ans=answer.objects.filter(questionId=id)
   usrs=user.objects.all()
   try:
       que=question.objects.get(pk=id)
   except question.DoesNotExist:
       que = None
   
   if que == None:
       raise Http404 
   
   return render(request, 'question_page.html',{'page_obj':paginate(ans,request,2),'answers':ans,'que':question.objects.get(pk=id),'users':user.objects.all()})
   
    
def tag(request,tg):
    
    temp_que=question.objects.filter(tag__tag=tg)

    if len(temp_que)>0:
        return render(request,'listing.html',{'page_obj':paginate(temp_que,request,4),'questions':temp_que, 'pagename':'Results searching by '+tg,'linkname':'New Questions','link':'main'})

    else:
        raise Http404

def pageNotFound(request,exception):
    return HttpResponseNotFound()