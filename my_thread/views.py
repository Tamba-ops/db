from django.db import connection, IntegrityError
from django.views.decorators.csrf import csrf_exempt
from util.parsers import parse_post
from util.queries import queries
from util.responses import *
from util.basic_functions import update_boolean_field,\
    create_basic, get_details_basic, handle_response,\
    list_basic, vote, update


@csrf_exempt
def create(request):
    return create_basic(request, 'thread')


def details(request):
    thread = request.GET.get('thread')

    if not thread:
        return response_code_3

    related = request.GET.getlist('related')
    return handle_response(get_details_thread(thread, related))


def get_details_thread(thread, related=None):
    return get_details_basic(thread, 'thread', related)


@csrf_exempt
def update_thread(request):
    return update(request, 'thread', ['slug', 'message'])


@csrf_exempt
def close_thread(request):
    return update_boolean_field(request, 'thread', 'close')


@csrf_exempt
def open_thread(request):
    return update_boolean_field(request, 'thread', 'open')


@csrf_exempt
def remove_thread(request):
    return change_thread_availability(request, 'remove')


@csrf_exempt
def restore_thread(request):
    return change_thread_availability(request, 'restore')


def change_thread_availability(request, action):
    request_post = parse_post(request)
    thread = request_post.get('thread')
    if not thread:
        return response_code_3

    cursor = connection.cursor()
    cursor.execute(queries['query_' + action + '_posts_in_deleted_thread'], thread)

    return update_boolean_field(request, 'thread', action)



@csrf_exempt
def subscribe(request):
    return change_subscription_status(request, 'insert')


@csrf_exempt
def unsubscribe(request):
    return change_subscription_status(request, 'delete')


@csrf_exempt
def change_subscription_status(request, action):
    cursor = connection.cursor()

    request_post = parse_post(request)
    thread_id = request_post.get('thread')
    user = request_post.get('user')
    if not thread_id or not user:
        return response_code_3

    query_change = 'query_subscriptions_' + action

    try:
        cursor.execute(queries[query_change], [user, thread_id])
    except IntegrityError:
        return create_response_code_5('cannot change subscription status')

    return create_response_code_0({"thread": thread_id,
                                   "user": user})


def list_threads(request):
    return list_basic(request, 'thread')


def list_posts(request):
    return list_basic(request, 'post')


@csrf_exempt
def vote_thread(request):
    return vote(request, 'thread')
