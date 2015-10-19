from util.responses import *
from util.basic_functions import update,\
    create_basic, get_details_basic, handle_response,\
    update_boolean_field, list_basic, vote


def create(request):
    return create_basic(request, 'post')


def details(request):
    post = request.GET.get('post')

    if not post:
        return response_code_3

    related = request.GET.getlist('related')

    return handle_response(get_details_post(post, related))


def get_details_post(post_id, related=None):
    return get_details_basic(post_id, 'post', related)


def list_posts(request):
    return list_basic(request, 'post')


def remove_post(request):
    return update_boolean_field(request, 'post', 'remove')


def restore_post(request):
    return update_boolean_field(request, 'post', 'restore')


def vote_post(request):
    return vote(request, 'post')


def update_post(request):
    return update(request, 'post', ['message'])
