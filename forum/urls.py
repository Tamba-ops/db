from django.conf.urls import url, patterns
from my_thread.views import list_threads
from post.views import list_posts
from forum.views import create, details, list_users

urlpatterns = patterns('',
                       url(r'^create', create),
                       url(r'^details', details),
                       url(r'^listPosts', list_posts),
                       url(r'^listThreads', list_threads),
                       url(r'^listUsers', list_users),
                       )

__author__ = 'fatman'

