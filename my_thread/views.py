from django.db import connection, IntegrityError
from util.queries import queries
from util.responses import *
from util.basic_functions import update_boolean_field,\
    create_basic, get_details_basic, handle_response,\
    list_basic, vote, update


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


def update_thread(request):
    return update(request, 'thread', ['slug', 'message'])


def close_thread(request):
    return update_boolean_field(request, 'thread', 'close')


def open_thread(request):
    return update_boolean_field(request, 'thread', 'open')


def remove_thread(request):
    return update_boolean_field(request, 'thread', 'remove')


def restore_thread(request):
    return update_boolean_field(request, 'thread', 'restore')


def subscribe(request):
    change_subscription_status(request, 'insert')


def unsubscribe(request):
    change_subscription_status(request, 'delete')


def change_subscription_status(request, action):
    cursor = connection.cursor()

    thread_id = request.GET.get('thread')
    user = request.GET.get('user')
    if not thread_id or not user:
        return response_code_3

    query_change = 'query_subscriptions_' + action

    try:
        cursor.execute(query_change, [user, thread_id])
    except IntegrityError:
        return create_response_code_5('cannot change subscription status')

    return create_response_code_0({"thread": thread_id,
                                   "user": user})


def list_threads(request):
    return list_basic(request, 'thread')


def list_posts(request):
    return list_basic(request, 'post')


def vote_thread(request):
    return vote(request, 'thread')
