# coding=utf-8
from django.db import connection, IntegrityError
from django.views.decorators.csrf import csrf_exempt
from util.basic_functions import \
    create_basic, get_details_basic, handle_list_request, \
    update, list_basic, validate_response, convert_fields_to_json
from util.errors import Code3Exception, Code5Exception
from util.queries import queries
from util.responses import *
from util.parsers import parse_post


@csrf_exempt
@validate_response
def create(request):
    return create_basic(request, 'user')


@validate_response
def details(request):
    email = request.GET.get('user')

    if not email:
        raise Code3Exception

    return create_response_code_0(get_details_basic(email, 'user'))


@validate_response
def list_followers(request):
    return list_follow_relations(request, 'followers')


@validate_response
def list_following(request):
    return list_follow_relations(request, 'following')


@validate_response
def list_follow_relations(request, entity):
    email = request.GET.get('user')
    if not email:
        raise Code3Exception

    data = []
    query = handle_list_request(request, queries['query_' + entity + '_user_full'], data)

    data.append(email)
    cursor = connection.cursor()
    cursor.execute(query, data)

    result = []
    for row in cursor:
        result.append(convert_fields_to_json(row, 'user'))

    # cursor.close()

    return create_response_code_0(result)


@csrf_exempt
@validate_response
def follow(request):
    return change_followers(request, queries['query_insert_follower'],
                            "Follower already exists")


@csrf_exempt
@validate_response
def unfollow(request):
    return change_followers(request, queries['query_delete_follower'],
                            "Wait , what?")


@csrf_exempt
@validate_response
def change_followers(request, query, message):
    request_post = parse_post(request)
    follower_email = request_post.get('follower')
    followee_email = request_post.get('followee')

    if not follower_email or not followee_email:
        raise Code3Exception

    cursor = connection.cursor()

    try:
        cursor.execute(query, [follower_email, followee_email])
    except IntegrityError:
        raise Code5Exception(message)

    # cursor.close()

    return create_response_code_0(get_details_basic(follower_email, 'user'))


@csrf_exempt
@validate_response
def update_profile(request):
    return update(request, 'user', ['name', 'about'])


@validate_response
def list_posts(request):
    return list_basic(request, 'post')
