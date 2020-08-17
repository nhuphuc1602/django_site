from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import django.utils.safestring as safestring


class Posts(models.Model):
    name = models.CharField("Name", max_length=200)
    author = models.CharField("Author", max_length=100)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    description = models.TextField("Description")
    upload_day = models.DateField("Day upload", max_length=50)

    def __str__(self):
        return self.name