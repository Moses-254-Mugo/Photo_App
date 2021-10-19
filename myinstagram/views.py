from django.contrib.auth import authenticate
from django.core.checks import messages
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from myinstagram.models import  Post, Profile, Comment, Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import  PostForm, CommentForm,ProfileUpdateForm,UserUpdateForm,CreateUserForm
from django.contrib.auth import logout,login
from django.contrib import messages




#Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all()
    user = request.user
    
    return render(request, 'index.html',{'posts':posts,'user': user})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'author' in request.GET and request.GET["author"]:
        search_term = request.GET.get("author")
        searched_articles = Post.search_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"categories": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid:
            post = form.save(commit= False)
            post.author = current_user
            post.save()
        return redirect('post_list')
    else:
        form = PostForm()
    return render(request,'create_post.html',{'form':form})


@login_required(login_url='/accounts/login/')
def comment_create(request,pk):
    post = Post.objects.get(pk = pk)
    form = CommentForm(request.POST,instance=post)
    if request.method == "POST":
        if form.is_valid():
            post = request.user.username
            comment = form.cleaned_data['comment']
            moo = Comment(post = post,comment =comment)
            moo.save()
            return redirect('index')
        else:
            print('form is invalid')
    else:
        form = CommentForm
    context = {
        'form':form
    }
    return render(request,'comment.html',context)

@login_required(login_url='login')
def create_post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid:
            post = form.save(commit= False)
            post.author = current_user
            post.save()
        return redirect('index')
    else:
        form = PostForm()
    return render(request,'new_post.html',{'form':form})




def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        phone_post = Post.objects.get(id= post_id)
        if user in phone_post.liked.all():
            phone_post.liked.remove(user)
        else:
            phone_post.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id = post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect('index')


def profile(request):
    user = request.user
    user = Profile.objects.get_or_create(user= request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)                         
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user

    }

    return render(request, 'profile.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')


    context = {'form': form}
    return render(request,'registraion/registration_form.html',context)

def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username = username,password= password)
        if user is not None:
            login(request,user)
            return redirect('index')
            
        else:
            messages.info(request,'Username or password is inorrect')
            

    context = {}
    return render(request,'registration/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')