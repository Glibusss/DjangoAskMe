from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.core.paginator import Paginator
from website.models import ANSWERS, QUESTIONS, question,answer,user






def paginate(obj_list, request, per_page=1):

    paginator=Paginator(obj_list,per_page)

    page_number = request.GET.get('page')

    page_obj=paginator.get_page(page_number)
    
    return page_obj
   

# Create your views here.


def listing(request):
    return render(request,'listing.html',{'page_obj':paginate(question.objects.orderByDate(),request,4),'pagename':'New Questions','linkname':'Hot questions','link':'hots'})
    
    
def login(request):
    return render(request,'login_form.html')


def registration(request):
    return render(request, 'reg_form.html')


def hot(request):
    return render(request,'listing.html',{'page_obj':paginate(question.objects.orderByRating(),request,4),'pagename':'Hot questions','linkname':'New Questions','link':'main'})
    
    

def ask(request):                                     
    return render(request,'question_form_login.html')


def questions(request,id):
   
   if question.objects.findId(id) == None:
       raise Http404 
   ans=answer.objects.sortByTop(id)
   return render(request, 'question_page.html',{'page_obj':paginate(ans,request,2),'answers':ans,'que':question.objects.findId(id)})
   
    
def tag(request,tg):
    
    temp_que=question.objects.filterTagByDate(tg)

    if len(temp_que)>0:
        return render(request,'listing.html',{'page_obj':paginate(question.objects.filterTagByDate(tg),request,4),'pagename':'Results searching by '+tg,'linkname':'New Questions','link':'main'})

    else:
        raise Http404

def pageNotFound(request,exception):
    return HttpResponseNotFound()