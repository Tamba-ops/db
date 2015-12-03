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
        "isSpam"
    ],

    "post_additional": [
        "likes",
        "dislikes",
        "points",
        "mpath"
    ]
}

__author__ = 'fatman'
