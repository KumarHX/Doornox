from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jobapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'), # about
    url(r'^(?P<access_token>[^/]+)/fblogin/$', views.fblogin, name='fblogin'),
    url(r'^googlogin/$', views.googlogin, name='googlogin'), 
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^(?P<user_id>[^/]+)/publicprofile/$', views.publicprofile, name='publicprofile'),
    # url(r'^[ALL JOB MODEL FIELD VALUES AVAILABLE]/addjob/$', views.lnkdlogin, name='lnkdlogin'),
    # url(r'^googconnect/$', views.googconnect, name='googconnect'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^lnkdconnect/$', views.lnkdconnect, name='lnkdconnect'),
    url(r'^contactus/$', views.contactus, name='contactus'), # slash issue
    url(r'^inbox/$', views.inbox, name='inbox'),
    url(r'^getmessages/$', views.getmessages, name='getmessages'),
    url(r'^sendmessage/$', views.sendmessage, name='sendmessage'),
    url(r'^sendmessagewithattachment/$', views.sendmessagewithattachment, name='sendmessagewithattachment'),
    url(r'^searchjobs/$', views.searchjobsall, name='searchjobsall'), 
    url(r'^(?P<search_input>[^/]+)/searchjobs/$', views.searchjobs, name='searchjobs'),
    url(r'^(?P<jobid>[^/]+)/job/$', views.job, name='job'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^update_user/$', views.update_user, name='update_user'),
    url(r'^getthreadpartners/$', views.getthreadpartners, name='getthreadpartners'),
    url(r'^(?P<partnerid>[^/]+)/getthread/$', views.getthread, name='getthread'),
    url(r'^markthreadasread/$', views.markthreadasread, name='markthreadasread'),
    url(r'^signin/$', views.onlysignin, name='onlysignin')
)
# these are urls