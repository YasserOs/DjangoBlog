from django.urls import path 
from . import views
from .views import allPosts, categoryPosts, showPost, postEdit  , postDelete , addCategory

urlpatterns = [

    path('home/', allPosts, name="allposts"),
    path('home/cat/<categoryID>', categoryPosts, name="article_detail"),
    path('post/<postID>', showPost, name="add_category"),
    path('editpost/<postID>', postEdit, name="update_post"),
    path('deletepost/<postID>', postDelete, name="delete_post"),
    path('add_cat/',addCategory,name='category'),
   
]