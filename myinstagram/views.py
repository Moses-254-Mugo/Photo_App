from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from myinstagram.models import Images
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import MyinstagramImageForm, MyinstagramSignUpForm,MyinstagramCommentsForm, MyinstagramUpdateUserForm, MyinstagramUpdateUserProfileForm


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='login')
def Home(request):
    pics = Images.objects.all()
    users = User.exclude(id=request.user.id)

    if request.method == 'POST':
        form = MyinstagramImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user =request.user.profile
            image.save()
            return HttpResponseRedirect(request.path_info)
        else:
            form = MyinstagramImageForm()
        params ={
            'pics':pics,
            'form': form,
            'users': users,

        }
        return render(request, 'Home.html', params)

@login_required(login_url='login')
def profile(request, username):
    pictures = request.user.profile.images.all()
    if request.method == 'POST':
        userform = MyinstagramUpdateUserForm(request.POST, instance=request.user)
        profileform = MyinstagramUpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()

            return HttpResponseRedirect(request.path_info)
        else:
            userform = MyinstagramUpdateUserForm(instance=request.user)
            profileform = MyinstagramUpdateUserProfileForm(instance=request.user.profile)
        params = {
            'userform': userform,
            'profileform': profileform,
            'pictures': pictures,
        }
        return render(request, 'profile.html', params)



def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})