from django.urls import path #,include
from . import views

from appadmin import views as adminView
from .views import AddPostView, DetailView, UpdatePost, DeletePost  , CategoryView,viewcategory
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/cat/<catID>', views.categories, name="categories"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add-category/', CategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePost.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePost.as_view(), name="delete_post"),
    path('login',views.loginPg , name='login'),
    path('signup',views.signupPg , name='signup'),
    path('signout',views.signoutPg , name='signout'),
    path('admin_panel',adminView.AdminPanel , name='admin_panel'),
    path('category/<cats>',views.viewcategory , name='category'),   
    path('post/<postID>', views.showPost, name="post"),
    path('Subscribe/<catid>',views.Subscribe , name='Subscribe'),
    path('Unsubscribe/<catid>',views.Unsubscribe , name='Unsubscribe'),
]