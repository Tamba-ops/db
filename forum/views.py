# coding=utf-8
from django.views.decorators.csrf import csrf_exempt
from util.errors import Code3Exception
from util.basic_functions import create_basic, get_details_basic, list_basic, validate_response
from util.responses import create_response_code_0


@csrf_exempt
@validate_response
def create(request):
    return create_basic(request, 'forum')


def get_details_forum(short_name, related=None):
    return get_details_basic(short_name, 'forum', related)


@validate_response
def details(request):
    short_name = request.GET.get('forum')
    if not short_name:
        raise Code3Exception

    related = request.GET.get('related')

    return create_response_code_0(get_details_forum(short_name, related))


@validate_response
def list_users(request):
    return list_basic(request, 'user')
