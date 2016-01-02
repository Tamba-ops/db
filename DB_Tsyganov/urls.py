# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from util.basic_functions import clear, status

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'DB_Tsyganov.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^db/api/forum/', include('forum.urls')),
                       url(r'^db/api/post/', include('post.urls')),
                       url(r'^db/api/thread/', include('my_thread.urls')),
                       url(r'^db/api/user/', include('my_user.urls')),
                       url(r'^db/api/clear/', clear),
                       url(r'^db/api/status/', status),
                       )
