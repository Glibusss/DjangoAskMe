import math
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator
from website.models import questions, answers

def paginate(obj_list, request, per_page=1):

    paginator=Paginator(obj_list,per_page)

    page_number = request.GET.get('page')

    page_obj=paginator.get_page(page_number)
    
    return page_obj
   

# Create your views here.
def listing(request):
        
    return render(request,'listing.html',{'page_obj':paginate(questions,request,4),'questions':questions,'pagename':'New Questions','linkname':'Hot questions','link':'hots'})
    
    
def login(request):
    return render(request,'login_form.html')


def registration(request):
    return render(request, 'reg_form.html')


def hot(request):

    return render(request,'listing.html',{'page_obj':paginate(questions,request,4),'questions':questions,'pagename':'Hot questions','linkname':'New Questions','link':'main'})
    
    

def ask(request):
    if request.GET.get('question')!= None and request.GET.get('qdescription')!= None and request.GET.get('tags')!= None:
       questions.append(
       { 'id': len(questions)+4,
        'title': request.GET.get('question'),
        'text': request.GET.get('qdescription'),
        'tags':request.GET.get('tags'),})
                                            
    return render(request,'question_form_login.html')


def question(request,id):
   for question in questions:
        if id in question.values():
           return render(request, 'question.html',{'page_obj':paginate(answers,request,2),'answers':answers,'question':question})

    
def tag(request,tg):
    temp_que = []
    for question in questions:
        if tg in question.values():
           temp_que.append(question)

    if len(temp_que)>0:
        return render(request,'listing.html',{'page_obj':paginate(temp_que,request,4),'questions':temp_que, 'pagename':'Results searching by '+tg,'linkname':'New Questions','link':'main'})


def pageNotFound(request,exception):
    return HttpResponseNotFound()