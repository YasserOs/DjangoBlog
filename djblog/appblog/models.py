from distutils.command import upload
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

from pymysql import NULL

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    publish_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=120, default='uncategorized')
    image = models.ImageField(null=True, blank=True, upload_to="appblog/images/")

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article_detail', args={str(self.id)})
        return reverse('home')


