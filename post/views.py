# coding=utf-8
from django.views.decorators.csrf import csrf_exempt
from util.errors import Code3Exception
from util.basic_functions import update,\
    create_basic, get_details_basic,\
    update_boolean_field, list_basic, vote, validate_response
from util.responses import create_response_code_0


@csrf_exempt
@validate_response
def create(request):
    return create_basic(request, 'post')


@validate_response
def details(request):
    post = request.GET.get('post')

    if not post:
        raise Code3Exception

    related = request.GET.getlist('related')

    return create_response_code_0(get_details_post(post, related))


def get_details_post(post_id, related=None):
    return get_details_basic(post_id, 'post', related)


@validate_response
def list_posts(request):
    return list_basic(request, 'post')


@csrf_exempt
@validate_response
def remove_post(request):
    return update_boolean_field(request, 'post', 'remove')


@csrf_exempt
@validate_response
def restore_post(request):
    return update_boolean_field(request, 'post', 'restore')


@csrf_exempt
@validate_response
def vote_post(request):
    return vote(request, 'post')


@csrf_exempt
@validate_response
def update_post(request):
    return update(request, 'post', ['message'])
