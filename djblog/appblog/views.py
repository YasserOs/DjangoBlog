from django.shortcuts import render 
from django.views.generic import (
    ListView as lv, 
    DetailView as dv,
    CreateView as cv,
    UpdateView as uv,
    DeleteView as delv, 
 )

from .models import  Post, Category
from .forms import   PostForm, EditForm
from django.urls import reverse_lazy,reverse

class HomeView(lv):
    model = Post 
    template_name = 'home.html'
    ordering = ['-publish_date']

class DetailView(dv):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(cv):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class CategoryView(cv):
    model = Category
    form_class = PostForm
    template_name = 'add_category.html'


class UpdatePost(uv):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePost(delv):
    model = Post
    template_name = 'delete_post.html'
    #fields = ['title', 'title_tag', 'body']
    success_url = reverse_lazy("home")

