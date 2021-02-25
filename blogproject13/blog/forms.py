from django import forms
from blog.models import Post,Comment,Like
from django.contrib.auth.models import User

class CreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','body')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')

class LikeForm(forms.ModelForm):
    class Meta:
        model=Like
        fields=('uname',)

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password','email')
