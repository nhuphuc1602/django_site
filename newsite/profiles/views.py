from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from news.models import Posts
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class login_view(LoginView):
    template_name = 'login.html'

class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class RegisterView(TemplateView):
    template_name = 'register.html'