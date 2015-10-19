from django.conf.urls import url, patterns

from post.views import create, details, list_posts,\
    vote_post, remove_post, restore_post, update_post

urlpatterns = patterns('',
                       url(r'create', create),
                       url(r'details', details),
                       url(r'list', list_posts),
                       url(r'remove', remove_post),
                       url(r'restore', restore_post),
                       url(r'vote', vote_post),
                       url(r'update', update_post)
                       )

__author__ = 'DmitryTsyganov'
