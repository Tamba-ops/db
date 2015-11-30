# coding=utf-8
import json


def parse_boolean(data):
    if data == 'true' or data == 1 or data == '1':
        return True
    elif data == 'false' or data == 0 or data == '0':
        return False
    else:
        raise Exception("Boolean parameters must be 'true', 'false', '1', '0' or 1, 0")


def parse_like(value):
    if value == '-1' or value == -1:
        return 'dislike'
    if value == '1' or value == 1:
        return 'like'


def parse_post(data):
    print(data.body)
    new_data = data.body.decode('utf-8')
    print(new_data)
    resp = json.loads(new_data)
    print(resp)
    return json.loads(data.body.decode('utf-8'))


__author__ = 'fatman'
