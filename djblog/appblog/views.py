from unicodedata import category
from django.shortcuts import render 
from django.views.generic import (
    ListView as lv, 
    DetailView as dv,
    CreateView as cv,
    UpdateView as uv,
    DeleteView as delv, 
 )

from .models import  Post, Category,Like,Dislike
from .forms import   PostForm, EditForm,UserForm
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
    user=request.user
    if user.is_authenticated:
        if request.method=='POST':
            post_id=request.POST.get('post_id')
            post_object = Post.obgects.get(id=post_id)
            if user in post_object.liked.all():
                post_object.liked = post_object.liked.remove(user)
                post_object.disliked = post_object.disliked.add(user)
            else:
                post_object.liked = post_object.liked.add(user)
                post_object.disliked = post_object.disliked.remove(user)

            post_object.save()
    return redirect('allposts')

def dislikePost(request):
    user=request.user
    if user.is_authenticated:
        if request.method=='POST':
            post_id=request.POST.get('post_id')
            post_object = Post.obgects.get(id=post_id)
            if user in post_object.liked.all():
                post_object.liked = post_object.liked.remove(user)
                post_object.disliked = post_object.disliked.add(user)
            else:
                post_object.liked = post_object.liked.add(user)
                post_object.disliked = post_object.disliked.remove(user)

            post_object.save()
    return redirect('allposts')

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



