
# Register your models here.
from django.contrib import admin
from .models import Posts

class PostsModelAdmin(admin.ModelAdmin):  
    list_display = ('name','author', 'description','upload_day')
    search_fields = ('name',)
    
admin.site.register(Posts, PostsModelAdmin)