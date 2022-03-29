from pyexpat import model
from django.utils import timezone
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=120)
    subbed_users = models.ManyToManyField(User)
    def __str__(self):
        return self.name
 

class Tags(models.Model):
    name=models.CharField(max_length=120)
    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    publish_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags)
    liked = models.ManyToManyField(User, blank=True, default=None, related_name= 'liked')
    disliked = models.ManyToManyField(User, blank=True, default=None, related_name= 'disliked')
    image = models.ImageField(null=True , upload_to="images/")
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    def comments_count(self):
        return self.comment_set.all().count()
    def comments(self):
        return self.comment_set.all()

    


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    comment_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.body

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.value 