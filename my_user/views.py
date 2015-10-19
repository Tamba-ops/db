from django.db import connection, IntegrityError
from util.basic_functions import convert_to_one_array,\
    create_basic, get_details_basic, handle_response, handle_list_request, update
from util.queries import queries
from util.responses import *


def create(request):
    return create_basic(request, 'user')


def details(request):
    email = request.GET.get('email')

    if not email:
        return response_code_3

    return handle_response(get_details_user(email))


def get_details_user(email, query_followers=queries['query_followers_user_desc'],
                     query_following=queries['query_following_user_desc']):

    response = get_details_basic(email, 'user')

    cursor = connection.cursor()
    cursor.execute(query_followers, [email])
    response["followers"] = convert_to_one_array(cursor)

    cursor.execute(query_following, [email])
    response["following"] = convert_to_one_array(cursor)

    return response


def list_followers(request):
    email = request.GET.get('email')
    if not email:
        return response_code_3

    query = handle_list_request(request, queries['query_followers_user_desc'])

    return create_response_code_0(get_details_user(email, query_followers=query))


def list_following(request):
    email = request.GET.get('email')
    if not email:
        return response_code_3

    query = handle_list_request(request, queries['query_following_user_desc'])

    return create_response_code_0(get_details_user(email, query_following=query))


def follow(request):
    return change_followers(request, queries['query_insert_follower'],
                            "Follower already exists")


def unfollow(request):
    return change_followers(request, queries['query_delete_follower'],
                            "Wait , what?")


def change_followers(request, query, message):
    follower_email = request.GET.get('follower')
    followee_email = request.GET.get('followee')

    if not follower_email or not followee_email:
        return response_code_3

    cursor = connection.cursor()

    try:
        cursor.execute(query, [follower_email, followee_email])
    except IntegrityError:
        return create_response_code_5(message)

    return create_response_code_0(get_details_user(follower_email))


def update_profile(request):
    return update(request, 'user', ['name', 'about'])
