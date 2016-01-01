# coding=utf-8
from django.views.decorators.csrf import csrf_exempt
from util.responses import create_response_code_0


@csrf_exempt
def return_generic_user(request):
    print(request.POST)
    generic_user = {
        #"id": None,
        #"short_name": None,
        #"email": None
    }

    return create_response_code_0(generic_user)

__author__ = 'root'
