from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Images, Comments

class MyinstagramSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required.Inform a valid email address.')

    class Meta:
        model = User
        fields =('username', 'email','password1', 'password2')


class MyinstagramUpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class MyinstagramUpdateUserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio', 'name', 'user' ]


class MyinstagramImageForm(forms.ModelForm):

    class Meta:
        model = Images
        fields = ('image', 'caption')


class MyinstagramCommentsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add comments here...'


    class Meta:
        model = Comments
        fields = ('comment',)
