from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator
from website.models import ANSWERS, QUESTIONS


def paginate(obj_list, request, per_page=1):

    paginator=Paginator(obj_list,per_page)

    page_number = request.GET.get('page')

    page_obj=paginator.get_page(page_number)
    
    return page_obj
   

# Create your views here.


def listing(request):
    return render(request,'listing.html',{'page_obj':paginate(QUESTIONS,request,4),'pagename':'New Questions','linkname':'Hot questions','link':'hots'})
    
    
def login(request):
    return render(request,'login_form.html')


def registration(request):
    return render(request, 'reg_form.html')


def hot(request):
    return render(request,'listing.html',{'page_obj':paginate(QUESTIONS,request,4),'questions':QUESTIONS,'pagename':'Hot questions','linkname':'New Questions','link':'main'})
    
    

def ask(request):
    if request.GET.get('question')!= None and request.GET.get('qdescription')!= None and request.GET.get('tags')!= None:
       QUESTIONS.append(
       { 'id': len(QUESTIONS),
        'title': request.GET.get('question'),
        'text': request.GET.get('qdescription'),
        'tags':request.GET.get('tags'),})
                                            
    return render(request,'question_form_login.html')


def questions(request,id):
   for que in QUESTIONS:
        if id in que.values():
           return render(request, 'question_page.html',{'page_obj':paginate(ANSWERS,request,2),'answers':ANSWERS,'que':que})
    
   raise Http404 
    

    
def tag(request,tg):
    temp_que = []
    for question in QUESTIONS:
        if tg in question.values():
           temp_que.append(question)

    if len(temp_que)>0:
        return render(request,'listing.html',{'page_obj':paginate(temp_que,request,4),'questions':temp_que, 'pagename':'Results searching by '+tg,'linkname':'New Questions','link':'main'})

    else:
        raise Http404

def pageNotFound(request,exception):
    return HttpResponseNotFound()