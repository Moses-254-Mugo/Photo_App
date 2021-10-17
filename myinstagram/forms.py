from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from .models import Profile, Images, Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user', 'image_id']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =('profile_pic', 'bio', 'username')

class NewPostForm(forms.ModelForm):

    class Meta:
        model= Images
        exclude = ['user', 'likes']
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
