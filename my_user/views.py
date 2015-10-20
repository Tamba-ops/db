from django.db import connection, IntegrityError
from django.views.decorators.csrf import csrf_exempt
from util.basic_functions import convert_to_one_array,\
    create_basic, get_details_basic, handle_response, handle_list_request, update, list_basic
from util.queries import queries
from util.responses import *
from util.parsers import parse_post


@csrf_exempt
def create(request):
    return create_basic(request, 'user')


def details(request):
    email = request.GET.get('user')

    if not email:
        return response_code_3

    return handle_response(get_details_user(email))


def get_details_user(email, query_followers=queries['query_followers_user'],
                     query_following=queries['query_following_user']):

    response = get_details_basic(email, 'user')
    if isinstance(response, JsonResponse):
        return response

    cursor = connection.cursor()
    cursor.execute(query_followers, [email])
    response["followers"] = convert_to_one_array(cursor)

    cursor.execute(query_following, [email])
    response["following"] = convert_to_one_array(cursor)

    return response


def list_followers(request):
    return list_follow_relations(request, 'followers')


def list_following(request):
    return list_follow_relations(request, 'following')


def list_follow_relations(request, entity):
    email = request.GET.get('user')
    if not email:
        return response_code_3

    data = []
    query = handle_list_request(request, queries['query_' + entity + '_user'], data)

    data.append(email)
    cursor = connection.cursor()
    cursor.execute(query, data)

    followers = convert_to_one_array(cursor)

    result = []

    for follower in followers:
        result.append(get_details_user(follower))

    return create_response_code_0(result)


@csrf_exempt
def follow(request):
    return change_followers(request, queries['query_insert_follower'],
                            "Follower already exists")


@csrf_exempt
def unfollow(request):
    return change_followers(request, queries['query_delete_follower'],
                            "Wait , what?")


@csrf_exempt
def change_followers(request, query, message):
    request_post = parse_post(request)
    follower_email = request_post.get('follower')
    followee_email = request_post.get('followee')

    if not follower_email or not followee_email:
        return response_code_3

    cursor = connection.cursor()

    try:
        cursor.execute(query, [follower_email, followee_email])
    except IntegrityError:
        return create_response_code_5(message)

    return create_response_code_0(get_details_user(follower_email))


@csrf_exempt
def update_profile(request):
    return update(request, 'user', ['name', 'about'])


def list_posts(request):
    return list_basic(request, 'post')
