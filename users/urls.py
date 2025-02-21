from django.conf.urls import patterns, include, url
from users.views import *





urlpatterns = patterns('',
    
    url(r'^$', home, name='home'),
    url(r'^login/', login, name='login'),
    url(r'^register/', register, name='register'),
    url(r'^logout/', logout, name='logout'),
    






)