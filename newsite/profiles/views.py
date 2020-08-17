from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from news.models import Posts
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User

class login_view(LoginView):
    template_name = 'login.html'
    

class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ('username', 'email')
        field_classes = {'username': UsernameField}
       
        

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    
    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(
         username = data['username'],
         password = data['password1'], 
         email = data['email'] 
         )
        return redirect('register_ok')

class RegisterViewOK(TemplateView):
    template_name = 'register_ok.html'


class SiteLogoutView(LogoutView):
    template_name = 'logout.html'
 