# coding=utf-8
from django.http import JsonResponse


def create_response_code_0(response):
    return JsonResponse({"code": 0, "response": response})


def create_response_code_5(message):
    return JsonResponse({"code": 5, "response": message})


def create_response_code_1(message):
    return JsonResponse({"code": 1, "response": message})

response_code_3 = JsonResponse({"code": 3, "response": "required parameters are missing"})

__author__ = 'root'
