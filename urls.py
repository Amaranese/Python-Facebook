from django.conf.urls.defaults import patterns, include, url
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()
from django.conf import settings




urlpatterns = patterns('',
    url(r'^', include('users.urls')),
    url(r'^likes/', include('likes.urls')),
    url(r'^facebook/login/?$', 'users.fb_views.login', name = 'fblogin'),
    url(r'^facebook/authentication_callback/?$', 'users.fb_views.authentication_callback', name='fblogin_callback'),
    url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),










)