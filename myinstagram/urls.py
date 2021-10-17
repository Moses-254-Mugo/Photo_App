from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    # url(r'^$',views.index,name='Home'),
    # url(r'^search/', views.search_profile, name='search_results'),
    # url('^$',views.welcome,name = 'welcome'),
    
    # url(r'^single_post/(\d+)',views.single_post,name ='single_post')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)