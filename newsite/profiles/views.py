from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from news.models import Posts
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User

class login_view(LoginView):
    template_name = 'login.html'

class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class RegisterForm(UserCreationForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}
        

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

