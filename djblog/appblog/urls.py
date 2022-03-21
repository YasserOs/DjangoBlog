from django.urls import path 
from . import views
from .views import allPosts, categoryPosts, tagPosts, showPost, postEdit  , postDelete ,likePost, dislikePost, addCategory, addTag

urlpatterns = [

    path('home/', allPosts, name="allposts"),
    path('home/cat/<categoryID>', categoryPosts, name="article_detail"),
    path('home/tag/<tagID>', tagPosts, name="add_post"),
    path('post/<postID>', showPost, name="add_category"),
    path('editpost/<postID>', postEdit, name="update_post"),
    path('deletepost/<postID>', postDelete, name="delete_post"),
    path('like/',likePost,name='category'),
    path('dislike/',dislikePost,name='category'),
    path('add_cat/',addCategory,name='category'),
   
]