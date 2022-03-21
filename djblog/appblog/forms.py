from django import forms
from .models import Post, Comments, Category

class post_form(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':2})) # to change the size of text area field
    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'category')


class edit_post_form(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':2})) # to change the size of text area field
    class Meta:
        model = Post
        fields = ('title', 'body', 'image', 'category')

class comment_form(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Write Comment ...'})) # to change the size of text area field
    class Meta:
        model = Comments
        fields = ('body',)


class category_form(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category',)
