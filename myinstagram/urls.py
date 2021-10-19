from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    
    path('',views.index,name = 'index'),
    path('new/', views.create_post, name='post_create'),
    path('comments/<int:pk>/', views.comment_create, name='comments_list'),
    path('newpost/', views.create_post, name='newpost'),
    path('search_results/',views.search_results, name='search_results'),
    path('like/', views.like_post, name='like-post'),
    path('profile/', views.profile, name='profile'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('user/',views.logoutUser,name='logout'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)