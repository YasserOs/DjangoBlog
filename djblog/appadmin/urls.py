from django.urls import path #,include
from appblog import views

from . import views as adminView

urlpatterns = [
    path('',adminView.AdminPanel , name='admin_panel'),
    path('login',views.loginPg , name='login'),
    path('signup',views.signupPg , name='signup'),
    path('signout',views.signoutPg , name='signout'),
    path('admin_panel',adminView.AdminPanel , name='admin_panel'),
    path('admin_posts',adminView.adminPosts , name='admin_posts'),
    path('post-add',adminView.addPost , name='post-add'),
    path('post-edit/<post_id>',adminView.editPost , name='post-edit'),
    path('post-del/<post_id>',adminView.postDel , name='post-delete'),

    path('admin_users',adminView.adminUsers , name='admin_users'),
    path('user-block/<user_id>',adminView.userBlock , name='user-block'),
    path('user-promote/<user_id>',adminView.userPromote , name='user-promote'),

    # path('categ-add',adminView.addCategory , name='categ-add'),
    # path('categ-edit/<cat_id>',adminView.editCategory , name='categ-edit'),
    # path('categ-del/<cat_id>',adminView.categoryDelete , name='categ-delete'),
]