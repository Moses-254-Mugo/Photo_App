from django.contrib.auth import authenticate
from django.http import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.utils import html
from myinstagram.models import Follow, Images, Profile
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



@login_required(login_url='login')
def user_profile(requset, username):
    user_profile = get_object_or_404(User, username=username)
    if request.user == user_profile:
        return redirect('profile', username=request.user.username)
    user_image = user_profile.profile.images.all()

    followers = Follow.objects.filter(followed=user_profile.profile)
    follower_status = None
    for follower in followers:
        if request.user.profile == follower.follwer:
            follower_status = True
        else:
            follower_status = False
    params = {
        'user_profile': user_profile,
        'user_image': user_image,
        'followers': followers,
        'follower_status': follower_status
    }
    print(followers)
    return render(requset, 'user_profile.html', params)


@login_required(login_url='login')
def postComents(request, id):
    pic = get_object_or_404(Images, pk=id)
    is_like = False
    if pic.likes.filter(id=request.user.id).exists():
        is_like = True
    if request.method == 'POST':
        form = MyinstagramCommentsForm(request.POST)

        if form.is_valid():
            save_comment = form.save(commit=False)
            save_comment.images = pic
            save_comment.user =request.user.profile
            save_comment.save()
            return HttpResponseRedirect(request.path_info)
        
    else:
        form = MyinstagramCommentsForm()
        params = {
            'pic': pic,
            'form': form,
            'is_like': is_like,
            'total_likes': pic.total_likes()
        }
        return render(request, 'single_post.html', params)

def like_post(request):
    image = get_object_or_404(Profile, id=request.POST.get('id'))
    is_like = False
    if  image.likes.filter(id=request.user.id).exitst():
        image.likes.remove(request.user)
        is_like= False
    else:
        image.likes.add(request.user)
        is_like = False

    params = {
        'image': image,
        'is_like': is_like,
        'total_likes': image.total_likes()
    }
    if request.is_ajax():
        html = render_to_response('like_section.html', params, request=request)
        return JsonResponse({'form': html})

@login_required(login_url='login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html',params)
    else:
        message = "You have not searched for any image"
    return render(request, 'search.html', {'message': message})


def follow(request,to_follow):
    if request.method == 'GET':
        userprofile3 = Profile.objects.get(pk=to_follow)
        s_follow =  Follow(follower=request.user.profile, followed=userprofile3)
        s_follow.save()
        
        return redirect('user_profile', userprofile3.user.username)