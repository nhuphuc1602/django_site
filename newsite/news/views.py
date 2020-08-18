from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from news.models import Posts

def index(request):
    response = HttpResponse()
    response.write("<h1>Welcome</h1>")
    response.write("This is the polls app")
    return response

def home_view(request):
    list_object = Posts.objects.all()
    return render(request, 'home.html', {'list_object' : list_object, 'nav' : 'home'})

def about_view(request):
    return render(request, 'about.html', {'nav' : 'about'})

def category_view(request):
    list_object = Posts.objects.all()
    return render(request, 'category.html', {'list_object' : list_object, 'nav' : 'home'})