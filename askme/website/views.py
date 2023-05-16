from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.urls import reverse
from website.models import Question,Answer,Profile,User,Tag
from website.forms import LoginForm, QuestionForm,RegistrationForm, AnswerForm
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.models import Sum

def paginate(objList, request, perPage=1):

    paginator=Paginator(objList,perPage)

    pageNumber = request.GET.get('page')

    pageObj=paginator.get_page(pageNumber)
    
    return pageObj
   

# Create your views here.




def listing(request):
    return render(request,'listing.html',{'page_obj':paginate(Question.objects.orderByDate(),request,4),
                                          'pagename':'New Questions',
                                          'linkname':'Hot questions',
                                          'link':'hots'}
                                          )

@login_required(login_url='/login/',redirect_field_name='continue')
def logout(request):
    auth.logout(request)
    return redirect('main',permanent=True)
    
@csrf_protect
def Login(request):
    if request.method=='GET':
        #TODO: continue
        return render(request,Login)
    if request.method == 'POST':
        userForm = LoginForm(request.POST)
        if userForm.is_valid():
            print(userForm.cleaned_data)
            user = auth.authenticate(**userForm.cleaned_data)
            if user:
                auth.login(request,user)
                return redirect(listing)
            else:
                return render(request,'login_form.html',{'Errortype':'Invalid data'})
            
    


def registration(request):
    if request.method == 'GET':
        return render(request, "reg_form.html")
    elif request.method == 'POST':
        regForm = RegistrationForm(request.POST)
        print(request.POST)
        
        if regForm.is_valid():
            if not regForm.checkPassword():
                return render(request, "reg_form.html",{'Errortype':'Passwords do not match'})

            if not regForm.checkMail():
                return render(request, "reg_form.html",{'Errortype':'User with this email already exists'})
            
            if not regForm.checkLogin():
                return render(request, "reg_form.html",{'Errortype':'User with this login already exists'})
            print(regForm.cleaned_data)
            user = User.objects.create_user(regForm.cleaned_data['username'], regForm.cleaned_data['email'], regForm.cleaned_data['password'])
            user.save()
            profile = Profile(profile=user,nickname=regForm.cleaned_data['nickname'])
            profile.save()
            
            return redirect('/login/')
    


def hot(request):
    return render(request,'listing.html',{'page_obj':paginate(Question.objects.orderByRating(),request,4),
                                          'pagename':'Hot questions',
                                          'linkname':'New Questions',
                                          'link':'main'}
                                          )
    
    
@login_required(login_url='/login/',redirect_field_name='continue')
def ask(request):  
    if request.method=='GET':
        return render(request,'question_form_login.html')
        
    if request.method == 'POST':
        
        form = QuestionForm(request.POST)

        if form.is_valid():
            
            if not form.good():
                return render(request,'question_form_login.html',{'Errortype':'Too many tags'})
            tagNames = form.cleaned_data['tags'].split() 
            newQuestion = Question(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['text'],
                authorId=Profile.objects.get(profile=request.user),
            )      
             
            print(tagNames) 
            newQuestion.save() 
            if len(tagNames)>0:
                if len(tagNames)>0 and not Tag.objects.findTag(tagNames[0]):
                    t=Tag(tag=tagNames[0])
                    t.save()
                    newQuestion.tag.add(t)
                else:
                    newQuestion.tag.add(Tag.objects.get(tag=tagNames[0]))
            if len(tagNames)>1:
                if  not Tag.objects.findTag(tagNames[1]):
                    t=Tag(tag=tagNames[1])
                    t.save()
                    newQuestion.tag.add(t)
                else:
                    newQuestion.tag.add(Tag.objects.get(tag=tagNames[1]))
            if len(tagNames)>2:
                if len(tagNames)>2 and not Tag.objects.findTag(tagNames[2]):
                    t=Tag(tag=tagNames[0])
                    t.save()
                    newQuestion.tag.add(t)
                else:
                    newQuestion.tag.add(Tag.objects.get(tag=tagNames[2]))

            return redirect('questions', id=newQuestion.id)
            
            


    


def questions(request,id):
   if request.method=='GET':
        if Question.objects.findId(id) == None:
            raise Http404 
        ans=Answer.objects.sortByTop(id)
        return render(request, 'question_page.html',{'page_obj':paginate(ans,request,2),
                                                'answers':ans,
                                                'que':Question.objects.findId(id)}
                                                )
   
   if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        print(form.data)
        que = Question.objects.findId(id)
        print(que)
        print(que.title)
        ans = Answer(
            txt=form.data['anstxt'],
            authorId=Profile.objects.get(profile=request.user),
            questionId=que,
            id=Answer.objects.getLastId()+1
        )
        ans.save()
        a=Answer.objects.sortByTop(id)
        i=0
        for c in a:
            i=i+1
            if c==ans:
                break
            

        return redirect(f"{reverse('questions', kwargs={'id':que.id})}?page={int(i/2)+i%2}")
   
   
   
    
def tag_search(request,tg):
    
    temp_que=Question.objects.filterTagByDate(tg)

    if len(temp_que)>0:
        return render(request,'listing.html',{'page_obj':paginate(Question.objects.filterTagByDate(tg),request,4),
                                              'pagename':'Results searching by '+tg,
                                              'linkname':'New Questions',
                                              'link':'main'}
                                              )

    else:
        raise Http404

@login_required
def settings(request):
    return render(request,'settings.html')


def pageNotFound(request,exception):
    return HttpResponseNotFound()


