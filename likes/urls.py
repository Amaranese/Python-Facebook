from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from FBHack.likes.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FBHack.views.home', name='home'),
    # url(r'^FBHack/', include('FBHack.urls')),
    url(r'^$', likes, name = 'like'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)