from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    
    url(r'^$',views.index,name = 'timeline'),
    url(r'^search/', views.results_search, name='search_results'),
    url(r'^profileupdae/$', views.update_prof, name='update_profile'),
    url(r'^comments/<int:id>/', views.comments, name='comments'),
    url(r'^singlepost/(\d+)', views.single_post, name='single_post'),
    url(r'^logout/$',views.request_logout,name ='logout'),
    url(r'^post/<int:post_id>/like',views.add_like,name ='schedule'),

    # url('^$',views.welcome,name = 'welcome'),
    
    #
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)