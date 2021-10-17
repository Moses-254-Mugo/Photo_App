from typing import Reversible
from django.contrib.auth import authenticate
from django.core.checks import messages
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from myinstagram.models import  Images, Profile, Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import EditProfileForm, NewPostForm, SignUpForm, CommentForm
from django.contrib.auth import logout


# #Create your views here.
# @login_required(login_url='/accounts/login/')
# def welcome(request):
#     return render(request, 'welcome.html')


@login_required(login_url='/accounts/login/')
def index(request):
    posts = Images.all_images()
    
    return render(request, 'index.html',{'posts':posts})


@login_required(login_url='/accounts/login/')
def profile(request):

    user_post = Images.user_picture(request.user)
    return render(request, 'profile.html', {'user_post': user_post})

@login_required(login_url='/accounts/login/')
def results_search(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        search_pics = Images.search_image(search_term)
        messages = f'{search_term}'
        

        return render(request, 'search.html', {'messages':messages, 'image':search_pics })

    else:
        message = "You've not searched anything."
        return render(request, 'search.html', {'message':message})


@login_required(login_url='/accounts/login/')
def update_prof(request):

    if request.method=='POST':
        form = EditProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'update_profile.html',{'form':form})


@login_required(login_url='/accounts/login/')
def comments(request, id):
    id=id
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(comment=False)
            comment.user = request.user
            img = Images.objects.get(id=id)
            comment.image_id= img
            comment.save()
            return redirect('update')

        else:
            image_id = id
            messages.Info(request, 'Fill all the fields correctly')
            return render('comment', id=image_id)
    else:
        id=id
        form = CommentForm()
        return render(request, 'comment.html', {'form':form, 'id': id})


@login_required(login_url='/accounts/login/')
def single_post(request, id):

    posts = Images.objects.get(id=id)
    comments = Comments.objects.filter(image_id = id)
    return render(request, 'single_post.html', {'posts':posts, 'comments':comments})



@login_required(login_url='/accounts/login/')
def request_logout(request):
    logout(request)
    return redirect('update')

@login_required(login_url='/accounts/login/')
def add_like(request, post_id):
    post = Images.objects.filter(pk=post_id).first()
    post.like += 1
    post.save()
    all_post = Images. all_images()
    context = {
        'picture':all_post,
    }
    return render(request, 'index.html', context)

@login_required(login_url='/accounts/login/')
def like_post(request,pk):
    post= get_object_or_404(Images, id=request.POST.get('post_id'))
    post.like.add(request.user) 
    return HttpResponseRedirect(Reversible('singlepost', args=[str(pk)]))