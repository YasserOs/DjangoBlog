from django import forms
from appblog.models import Post, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#choices = [('politics','politics'), ('sports', 'sports'), ('news', 'news')]
choices = Category.objects.all().values_list('name', 'name')

choices_list = []

for i in choices:
    choices_list.append(i)


class CategotyForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your name here!'}),
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        # fields = ('__all__')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','image','category', 'body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title here!'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value' : '' , 'id' : 'author', 'type': 'hidden'}),
            #'author' : forms.Select(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }
    
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title here!'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }

