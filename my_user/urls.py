from django.conf.urls import url, patterns

from my_user.views import create, details, follow, \
    list_followers, list_following, unfollow, update_profile, list_posts

urlpatterns = patterns('',
                       url(r'^create/$', create),
                       url(r'^details', details),
                       url(r'^follow', follow),
                       url(r'^listFollowers', list_followers),
                       url(r'^listFollowing', list_following),
                       url(r'^unfollow', unfollow),
                       url(r'^updateProfile', update_profile),
                       url(r'^listPosts', list_posts)
                       )

__author__ = 'fatman'
