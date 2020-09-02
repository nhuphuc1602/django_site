"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from news import views
from profiles import views as profile_view

urlpatterns = [
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('about/', views.about_view, name = 'about'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', profile_view.login_view.as_view(), name = 'login'),
    path('accounts/profile/', profile_view.EditProfileView.as_view(), name = 'profile'),
    path('register/', profile_view.RegisterView.as_view(), name = 'register'),
    path('register/ok/', profile_view.RegisterViewOK.as_view(), name = 'register_ok'),
    path('logout/', profile_view.SiteLogoutView.as_view(), name = 'logout'),
    path('category/', views.category_view, name = 'category'),
    path('moon/', views.moon_view, name = 'moon'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)