from django import forms
from website.models import Profile
from django.contrib.auth.forms import UserCreationForm


class QuestionForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    tags = forms.CharField()

    def good(self):
        cleaned_data = super().clean()
        tag_names = cleaned_data['tags'].split()
        if len(tag_names) > 3:
            return False
        return True


class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    nickname = forms.CharField()
    #avatar = forms.ImageField()
    password = forms.CharField()
    repeat_password = forms.CharField()
    
    def checkPassword(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['repeat_password']:
            return False
        return True
    

    def checkMail(self):
        cleaned_data = super().clean()
        try:
            print(cleaned_data['email'])
            profiles = Profile.objects.get(profile__email=cleaned_data['email'])
        except Profile.DoesNotExist:
                return True
        return False
    

    def checkLogin(self):
        cleaned_data = super().clean()
        try:
            profiles = Profile.objects.get(profile__username=cleaned_data['username'])
        except Profile.DoesNotExist:
                return True
        return False

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class AnswerForm(forms.Form):
    anstxt = forms.CharField()