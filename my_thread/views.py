# coding=utf-8
from django.db import connection, IntegrityError
from django.views.decorators.csrf import csrf_exempt
from util.errors import Code3Exception, Code5Exception
from util.parsers import parse_post
from util.queries import queries
from util.responses import *
from util.basic_functions import update_boolean_field,\
    create_basic, get_details_basic, \
    list_basic, vote, update, validate_response


@csrf_exempt
@validate_response
def create(request):
    return create_basic(request, 'thread')


@validate_response
def details(request):
    thread = request.GET.get('thread')

    if not thread:
        raise Code3Exception

    related = request.GET.getlist('related')
    return create_response_code_0(get_details_thread(thread, related))


def get_details_thread(thread, related=None):
    return get_details_basic(thread, 'thread', related)


@csrf_exempt
@validate_response
def update_thread(request):
    return update(request, 'thread', ['slug', 'message'])


@csrf_exempt
@validate_response
def close_thread(request):
    return update_boolean_field(request, 'thread', 'close')


@csrf_exempt
@validate_response
def open_thread(request):
    return update_boolean_field(request, 'thread', 'open')


@csrf_exempt
@validate_response
def remove_thread(request):
    return change_thread_availability(request, 'remove')


@csrf_exempt
@validate_response
def restore_thread(request):
    return change_thread_availability(request, 'restore')


@validate_response
def change_thread_availability(request, action):
    request_post = parse_post(request)
    thread = request_post.get('thread')
    if not thread:
        raise Code3Exception

    cursor = connection.cursor()
    cursor.execute(queries['query_' + action + '_posts_in_deleted_thread'], thread)
    # cursor.close()

    return update_boolean_field(request, 'thread', action)


@csrf_exempt
@validate_response
def subscribe(request):
    return change_subscription_status(request, 'insert')


@csrf_exempt
@validate_response
def unsubscribe(request):
    return change_subscription_status(request, 'delete')


@csrf_exempt
@validate_response
def change_subscription_status(request, action):

    request_post = parse_post(request)
    thread_id = request_post.get('thread')
    user = request_post.get('user')
    if not thread_id or not user:
        raise Code3Exception

    query_change = 'query_subscriptions_' + action

    cursor = connection.cursor()

    try:
        cursor.execute(queries[query_change], [user, thread_id])
    except IntegrityError:
        raise Code5Exception('cannot change subscription status')

    # cursor.close()
    return create_response_code_0({"thread": thread_id,
                                   "user": user})


@validate_response
def list_threads(request):
    return list_basic(request, 'thread')


@validate_response
def list_posts(request):
    return list_basic(request, 'post')


@csrf_exempt
@validate_response
def vote_thread(request):
    return vote(request, 'thread')
