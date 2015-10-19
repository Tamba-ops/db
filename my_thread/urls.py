from django.conf.urls import url, patterns

from my_thread.views import create, details, open_thread,\
    close_thread, list_threads, subscribe, unsubscribe, vote_thread,\
    update_thread, remove_thread, restore_thread, list_posts

urlpatterns = patterns('',
                       url(r'^create', create),
                       url(r'^details', details),
                       url(r'^close', close_thread),
                       url(r'^open', open_thread),
                       url(r'^listPosts', list_posts),
                       url(r'^remove', remove_thread),
                       url(r'^restore', restore_thread),
                       url(r'^list', list_threads),
                       url(r'^subscribe', subscribe),
                       url(r'^unsubscribe', unsubscribe),
                       url(r'^vote', vote_thread),
                       url(r'^update', update_thread)
                       )

__author__ = 'fatman'
