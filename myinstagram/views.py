from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http  import HttpResponse
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




def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})