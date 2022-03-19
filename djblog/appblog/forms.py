from django import forms
from django.forms import widgets
from .models import Post, Category

#choices = [('politics','politics'), ('sports', 'sports'), ('news', 'news')]
choices = Category.objects.all().values_list('name', 'name')

choices_list = []

for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author','category', 'body')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title here!'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value' : '' , 'id' : 'author', 'type': 'hidden'}),
            #'author' : forms.Select(attrs={'class': 'form-control', 'value'}),
            'category' : forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }
    
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title here!'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }

