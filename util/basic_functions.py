from django.db import connection, IntegrityError
from django.utils.datetime_safe import  date
from django.views.decorators.csrf import csrf_exempt
from util.data_info import positions
from util.parsers import parse_boolean
from util.responses import *
from util.queries import queries
from util.parsers import parse_like, parse_post


@csrf_exempt
def clear(request):
    cursor = connection.cursor()
    cursor.execute(queries['query_change_foreign_check'], 0)
    for entity in ['User', 'Forum', 'Thread', 'Post', 'Subscriptions', 'Followers']:
        cursor.execute(queries['query_delete'] + entity)
    cursor.execute(queries['query_change_foreign_check'], 0)
    return create_response_code_0('OK')


@csrf_exempt
def status(request):
    cursor = connection.cursor()
    response = {}

    for entity in ['user', 'thread', 'forum', 'post']:
        cursor.execute(queries['query_count_' + entity])
        response[entity] = cursor.fetchone()[0]

    return create_response_code_0(response)


def convert_fields_to_json(details, entity):
    result = {}
    fields = positions[entity + '_required'] +\
        positions[entity + '_optional'] + positions[entity + '_additional']

    entity_id = None

    for index, field in enumerate(fields):

        cursor = connection.cursor()
        if field == 'email' and entity == 'user':
            user_email = details[index]
        if field == 'id' and entity == 'thread':
            entity_id = details[index]
        if field == 'id' and entity == 'post':
            entity_id = details[index]
        if field == 'posts':
            cursor.execute(queries['query_count_posts_in_thread'], entity_id)
            posts = cursor.fetchone()
            if posts:
                posts = posts[0]
            else:
                posts = 0
            result[field] = convert_if_needed(field, posts)

        elif field == 'subscriptions':
            cursor.execute(queries['query_count_user_subscriptions'], user_email)
            subscriptions = convert_to_one_array(cursor)

            result[field] = convert_if_needed(field, subscriptions)
        elif field == 'mpath':
            field = 'parent'
            mpath_parent = details[index]

            cursor.execute(queries['query_find_id_of_parent'], mpath_parent[:-6])
            parent_id = cursor.fetchone()
            if parent_id:
                parent_id = parent_id[0]
            else:
                parent_id = None
            result[field] = convert_if_needed(field, parent_id)
        elif field == 'points':
            query_key = 'query_' + entity + '_points'
            cursor.execute(queries[query_key], entity_id)
            points = cursor.fetchone()[0]
            result[field] = convert_if_needed(field, points)
        else:
            result[field] = convert_if_needed(field, details[index])

    return result


def convert_if_needed(field, value):
    if field == 'date' and type(value) is not date:
        value = str(value).replace('+00:00', '')
        value = str(value).replace('+00:00', '')
    if check_boolean(field):
        return parse_boolean(value)
    return value


def create_mpath_number(new_id):
    mpath_number = '/'
    number_of_bits_total = 5

    number_of_bits_new_id = len(str(new_id))
    number_of_zeros = number_of_bits_total - number_of_bits_new_id

    for index in range(0, number_of_zeros):
        mpath_number += '0'

    mpath_number += str(new_id)

    return mpath_number


def create_mpath(parent_id):

    cursor = connection.cursor()

    if parent_id is not None:
        cursor.execute(queries['query_post_mpath'], parent_id)
        mpath = cursor.fetchone()[0]
        cursor.execute(queries['query_count_post_in_tree'], mpath[:6] + '%')
    else:
        mpath = ''
        cursor.execute(queries['query_count_post'])

    new_id = cursor.fetchone()[0]

    mpath_number = create_mpath_number(new_id)

    mpath += mpath_number

    return mpath


def create_basic(request, entity):

    required_parameters_names = positions[entity + '_required']
    optional_parameters_names = positions[entity + '_optional']

    data = []
    all_parameters = {}
    request_post = parse_post(request)

    for name in required_parameters_names:
        if name != 'id':
            parameter = request_post.get(name, 'iNone')
            data.append(convert_if_needed(name, parameter))
            all_parameters[name] = convert_if_needed(name, parameter)

    for value in data:
        if value == 'iNone':
            return response_code_3

    if entity == 'post':
        data.append(create_mpath(request_post.get('parent')))

    query_create_key = 'query_insert_' + entity
    query_create = queries[query_create_key]
    cursor = connection.cursor()

    for name in optional_parameters_names:
        parameter = request_post.get(name, 'iNone')
        if parameter != 'iNone':
            query_create += ', ' + name + ' = %s'
            data.append(convert_if_needed(name, parameter))
            all_parameters[name] = convert_if_needed(name, parameter)
        else:
            if name == 'parent':
                all_parameters[name] = None
            else:
                all_parameters[name] = False

    try:
        cursor.execute(query_create, data)
    except IntegrityError:
        message = 'Cannot create ' + entity
        return create_response_code_5(message)

    query_id_key = 'query_select_max_id_' + entity
    query_id = queries[query_id_key]

    cursor.execute(query_id)

    all_parameters['id'] = cursor.fetchone()[0]

    resp = create_response_code_0(all_parameters)

    return resp


def get_details_basic(key, entity, related=None):
    cursor = connection.cursor()
    query_select_key = 'query_select_' + entity

    cursor.execute(queries[query_select_key], [key])
    row = cursor.fetchall()

    message = 'There is no such ' + entity
    if not row:
        return create_response_code_1(message)

    return handle_related_entities(related, convert_fields_to_json(row[0], entity))


def handle_related_entities(related, response):
    if related:
        if 'forum' in related:
            forum = response.get('forum', 'iNone')
            if forum == 'iNone':
                return response_code_3
            response['forum'] = get_details_basic(forum, 'forum')
        if 'user' in related:
            user = response.get('user', 'iNone')
            if user == 'iNone':
                return response_code_3
            from my_user.views import get_details_user
            response['user'] = get_details_user(user)
        if 'thread' in related:
            thread = response.get('thread', 'iNone')
            if thread == 'iNone':
                return response_code_3
            response['thread'] = get_details_basic(thread, 'thread')

    return response


def convert_to_one_array(cursor):
    return [row[0] for row in cursor.fetchall()]


def handle_response(response):
    if isinstance(response, JsonResponse):
        return response

    return create_response_code_0(response)


# considering that all boolean field names start with 'is'
def check_boolean(field_name):
    key_array = list(field_name)
    return key_array[0] == 'i' and key_array[1] == 's'


def handle_list_request(request, query, data=None):

    sort = request.GET.get('sort')
    query_where = ' WHERE'
    if sort:
        if sort == 'parent_tree':
            limit = request.GET.get('limit')
            if limit:
                if data is None:
                    raise Exception("Request with 'sort' parameter "
                                    "requires 'data' list as third argument "
                                    "of 'parse_list_request' function'.")

                query_where_new = ' WHERE mpath < %s AND'
                query = query.replace(query_where, query_where_new)
                data.insert(0, create_mpath_number(limit))
        if sort != 'flat':
            query = query.replace('ORDER BY date', 'ORDER BY mpath')

    order = request.GET.get("order")
    if order == 'asc':
        query = query.replace('DESC', 'ASC')

    since = request.GET.get('since')
    if since:
        if data is None:
            raise Exception("Request with 'since' parameter "
                            "requires 'data' list as third argument "
                            "of 'parse_list_request' function'.")
        data.insert(0, since)
        query_where_new = ' WHERE date > %s AND'
        if query.find(query_where) != -1:
            query = query.replace(query_where, query_where_new)
        else:
            query += query_where_new[:-4]

    since_id = request.GET.get('since_id')
    if since_id:
        if data is None:
            raise Exception("Request with 'since_id' parameter "
                            "requires 'data' list as third argument "
                            "of 'parse_list_request' function'.")
        data.insert(0, int(since_id))
        query_where_new = ' WHERE id >= %s AND'
        query_where_user = ' WHERE u.id >= -2'
        if query.find(query_where_user) != -1:
            query = query.replace(query_where_user, query_where_user[:-2] + '%s')
        elif query.find(query_where) != -1:
            query = query.replace(query_where, query_where_new)
        else:
            query += query_where_new[:-4]

    limit = request.GET.get('limit')
    if limit and sort != 'parent_tree':
        query += ' LIMIT ' + str(limit)

    return query


def list_basic(request, entity):
    forum = request.GET.get('forum')
    user = request.GET.get('user')
    thread = request.GET.get('thread')

    cursor = connection.cursor()

    if user:
        key = user
        query_string = 'user'
    elif forum:
        key = forum
        query_string = 'forum'
    elif thread:
        key = thread
        query_string = 'thread'
    else:
        return response_code_3

    query_key = 'query_list_' + entity + 's_' + query_string

    query = queries[query_key]

    data = []
    query = handle_list_request(request, query, data)
    if query_string == 'forum' and entity == 'user':
        data.insert(0, key)
    else:
        data.append(key)

    cursor.execute(query, data)

    result_ids = convert_to_one_array(cursor)
    related = request.GET.getlist('related')

    for index, entity_id in enumerate(result_ids):
        if entity == 'user':
            from my_user.views import get_details_user
            temp = get_details_user(entity_id)
        else:
            temp = get_details_basic(entity_id, entity, related)
        if not isinstance(temp, JsonResponse):
            result_ids[index] = temp
        else:
            return create_response_code_5('Related entities are missing')

    return create_response_code_0(result_ids)


def update_boolean_field(request, entity, action):
    cursor = connection.cursor()
    entity_key = parse_post(request)[entity]
    if not entity_key:
        return response_code_3

    query_update = 'query_update_' + entity + '_' + action

    cursor.execute(queries[query_update], [entity_key])
    return create_response_code_0({entity: entity_key})


def vote(request, entity):
    request_post = parse_post(request)
    entity_key = request_post.get(entity)
    like = request_post.get('vote')

    if not entity_key or not like:
        return response_code_3

    action = parse_like(like)

    query_vote_key = 'query_' + entity + 's_' + action

    cursor = connection.cursor()
    cursor.execute(queries[query_vote_key], entity_key)

    return create_response_code_0(get_details_basic(entity_key, entity))


def update(request, entity, parameters_to_change):

    request_post = parse_post(request)
    data = []

    for parameter in parameters_to_change:
        value = request_post.get(parameter)
        if value:
            data.append(value)
        else:
            return response_code_3

    entity_key = request_post.get(entity)

    if not entity_key:
        return response_code_3

    data.append(entity_key)

    cursor = connection.cursor()
    query_update_key = 'query_update_' + entity

    try:
        cursor.execute(queries[query_update_key], data)
    except IntegrityError:
        return create_response_code_5('cannot update ' + entity)

    if entity == 'user':
        from my_user.views import get_details_user
        response = get_details_user(entity_key)
    else:
        response = get_details_basic(entity_key, entity)

    return handle_response(response)

__author__ = 'root'
