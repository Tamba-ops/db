from util.responses import *
from util.basic_functions import create_basic, get_details_basic, handle_response, list_basic


def create(request):
    return create_basic(request, 'forum')


def get_details_forum(short_name, related=None):
    return get_details_basic(short_name, 'forum', related)


def details(request):
    short_name = request.GET.get('short_name')
    if not short_name:
        return response_code_3

    related = request.GET.get('related')

    return handle_response(get_details_forum(short_name, related))


def list_users(request):
    return list_basic(request, 'user')
