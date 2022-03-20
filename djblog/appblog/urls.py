from django.urls import path #,include
from . import views
from .views import AddPostView, DetailView, UpdatePost, DeletePost  , CategoryView #, CategoryPageView, LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.home, name="home"),
    path('article/<int:pk>', DetailView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add-category/', CategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePost.as_view(), name="delete_post"),
    path('login',views.loginPg , name='login'),
    path('signup',views.signupPg , name='signup'),
    path('signout',views.signoutPg , name='signout'),
    path('admin_panel',views.AdminPanel , name='admin_panel'),
    path('admin_posts',views.adminPosts , name='admin_posts'),
    path('post-add',views.addPost , name='post-add'),
    path('post-edit/<post_id>',views.editPost , name='post-edit'),
    path('post-del/<post_id>',views.postDel , name='post-delete')
    
]