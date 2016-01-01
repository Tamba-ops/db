# coding=utf-8
boolean_fields = {
    "isAnonymous",
    "isApproved",
    "isDeleted",
    "isEdited",
    "isHighlighted",
    "isSpam",
    "isDeleted",
    "isClosed"
}

columns_number = {
    "user": 6,
    "post": 15,
    "thread": 13,
    "forum": 4
}

positions = {
    "user_required": [
        "id",
        "about",
        "email",
        "name",
        "username"
    ],

    "user_optional": [
        "isAnonymous"
    ],

    "user_additional": [
        'subscriptions'
    ],

    "forum_required": [
        "id",
        "name",
        "short_name",
        "user"
    ],

    "forum_optional": [

    ],

    "forum_additional": [

    ],

    "thread_required": [
        'id',
        'date',
        'isClosed',
        'message',
        'slug',
        'title',
        'user',
        'forum'
    ],

    "thread_optional": [
        'isDeleted'
    ],

    "thread_additional": [
        'likes',
        'dislikes',
        'points',
        'posts'
    ],

    "post_required": [
        'id',
        'date',
        'message',
        'forum',
        'thread',
        'user'
    ],

    "post_optional": [
        "isApproved",
        "isDeleted",
        "isEdited",
        "isHighlighted",
        "isSpam",
        "parent"
    ],

    "post_additional": [
        "likes",
        "dislikes",
        "points",
        "mpath"
    ]
}

join = {
    "post": {
        "forum": " JOIN Forum ON Forum.short_name = Post.Forum_short_name",
        "thread": " JOIN Thread ON Thread.id = Post.thread",
        "user": " JOIN User ON User.email = Post.User_email"
    }
}

__author__ = 'fatman'
