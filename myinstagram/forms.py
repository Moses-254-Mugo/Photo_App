from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.fields import files
from django.forms import widgets
from .models import Profile, Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
        
        widgets = {
            'comment': forms.Textarea(attrs={'class':'formcontrol'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('post', 'post',css_class = 'btn btn-success'))

    class Meta:
        model = Post
        fields = [
            'image',
            'caption'
        ]
        

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']