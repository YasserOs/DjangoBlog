from django.shortcuts import render 
from django.views.generic import (
    ListView as lv, 
    DetailView as dv,
    CreateView as cv,
    UpdateView as uv,
    DeleteView as delv, 
 )

from .models import  Post, Category
from .forms import   PostForm, EditForm,UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect, render

# admin CRUD
@login_required(login_url='login')
def AdminPanel(request):
    if request.user.is_superuser:
        return render(request,'appblog/templates/AdminCRUD/admin_panel.html')

def adminPosts(request): 
    posts = Post.objects.all()
    context = { "object_list" : posts}
    return render(request,'appblog/templates/AdminCRUD/posts.html', context)

def addPost(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('admin_posts')
    post_form = PostForm()
    context = {'form': post_form}
    return render(request, 'appblog/templates/add_post.html', context)

def editPost(request, post_id):
    post = Post.objects.get(id=post_id)
    post_form = PostForm(instance=post)

    if request.method =='POST':
        post_form = PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('admin_posts')
    context={'form': post_form}
    return render(request, 'appblog/templates/add_post.html', context)
    
def postDel(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('admin_posts')
    
def home(request): 
    posts = Post.objects.all()
    context = { "object_list" : posts}
    return render(request,'appblog/templates/home.html', context)

def loginPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(username= name, password =passwd)
            if user is not None:
                login(request, user)
                if request.GET.get('next') is not None:
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
                
            else:
                messages.info(request, 'User name or password is incorrect')
        return render(request, 'appblog/templates/login.html')

def signoutPg(request):
    logout(request)
    return redirect('home')

def signupPg(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        signup_form = UserForm()
        if(request.method =='POST'):
            signup_form = UserForm(request.POST)
            if(signup_form.is_valid()):
                signup_form.save()
                msg = 'User account created for username: ' + signup_form.cleaned_data.get('username')
                messages.info(request, msg)
                return redirect('login')
        context = {'signup_form': signup_form}
        return render(request, 'appblog/templates/signup.html', context)



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

