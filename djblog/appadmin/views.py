from unicodedata import category
from django.shortcuts import render
from appblog.models import  Post ,Category
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from .forms import PostForm,CategotyForm
# Create your views here.
# admin CRUD
@login_required(login_url='login')
def AdminPanel(request):
    if request.user.is_superuser:
        return render(request,'appadmin/templates/admin_panel.html')

def adminPosts(request): 
    posts = Post.objects.all()
    context = { "object_list" : posts}
    return render(request,'appadmin/templates/posts.html', context)

def addPost(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('admin_posts')
    post_form = PostForm()
    context = {'form': post_form}
    return render(request, 'appadmin/templates/add_post.html', context)

def editPost(request, post_id):
    post = Post.objects.get(id=post_id)
    post_form = PostForm(instance=post)

    if request.method =='POST':
        post_form = PostForm(request.POST,request.FILES,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('admin_posts')
    context={'form': post_form}
    return render(request, 'appadmin/templates/add_post.html', context)
   
def postDel(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('admin_posts')
########## users

def adminUsers(request):
    users = User.objects.all()
    context = { "object_list" : users}
    return render(request,'appadmin/templates/users.html', context)

def userBlock(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active= not user.is_active
    user.save()
    return redirect('admin_users')

def userPromote(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_superuser= not user.is_superuser
    user.save()
    return redirect('admin_users')

########## categories

def adminCategories(request): 
    cats = Category.objects.all()
    context = { "object_list" : cats}
    return render(request,'appadmin/templates/categories.html', context)

def addCategory(request):
    if request.method == 'POST':
        category_form = CategotyForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('categ-page')
    category_form = CategotyForm()
    context = {'form': CategotyForm}
    return render(request, 'appadmin/templates/add_category.html', context)

def editCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    categotyForm = CategotyForm(instance=category)

    if request.method =='POST':
        categotyForm = CategotyForm(request.POST,instance=category)
        if categotyForm.is_valid():
            categotyForm.save()
            return redirect('categ-page')
    context={'form': categotyForm}
    return render(request, 'appadmin/templates/add_category.html', context)
   
def categoryDelete(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('categ-page')