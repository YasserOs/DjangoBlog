from cgitb import text
from multiprocessing import context
from unicodedata import category
from django.shortcuts import get_object_or_404, render 
from django.contrib.auth.models import User

from django.views.generic import (
    ListView as lv, 
    DetailView as dv,
    CreateView as cv,
    UpdateView as uv,
    DeleteView as delv, 
 )

from .models import  Post, Category, Like, Dislike, Comment
from .forms import   PostForm, EditForm,UserForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect, render


    
def home(request): 
    posts = Post.objects.all()
    categories= Category.objects.all()
    context = { "object_list" : posts,
                "categories" : categories
                }
                
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

def likePost(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
            post_obj.disliked.add(user)
        else:
            post_obj.liked.add(user)
            post_obj.disliked.remove(user)

        post_obj.save()
    return redirect('home')

def dislikePost(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.disliked.all():
            post_obj.disliked.remove(user)
            post_obj.liked.add(user)
        else:
            post_obj.disliked.add(user)
            post_obj.liked.remove(user)

        post_obj.save()

    return redirect('home')

def categories(request, catID):
   posts = Post.objects.filter(category=catID)
   form = PostForm()
   categories= Category.objects.all()
   context={
       'allposts':posts,
       'form':form,
       'categories':categories,
   }
   return render (request,'home.html',context)

def viewcategory(request,cats):
     category_posts = Post.objects.filter(category=Category.objects.get(id=cats))
     return render (request,'categories.html',{'cats':cats.title(),'category_posts':category_posts})












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





def add_comment(request,_post):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('article_detail')
    comments = Comment.objects.get(post=_post)        
    context = {'comments': comment_form}
    return render(request, 'article_detail.html', context)    
       