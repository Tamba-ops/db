from django.core.management.base import BaseCommand
from django.db import connection

from util.queries import queries
from util.data_info import positions


def create_users(quantity):
    cursor = connection.cursor()

    for number in range(0, int(quantity)):

        data = []

        for key in positions["user_required"]:
            print("=", end="")
            if key != "id":
                data.append(str(key) + "_test_" + str(number))

        cursor.execute(queries['query_insert_user'], data)


def create_followers(quantity):
    cursor = connection.cursor()

    for number in range(0, int(int(quantity) / 2)):
        data = ["email_test_" + str(number), "email_test_" + str(number + 1)]
        cursor.execute(queries['query_insert_follower'], data)


class Command(BaseCommand):
    args = '<number of data to create>'
    help = 'creates specified number of users'

    def handle(self, *args, **options):
        create_users(args[0])
        create_followers(args[0])


__author__ = 'root'
