#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 11:31
# @Author  : Meng
# @File    : views.py
# @Software: PyCharm
from django.http import HttpResponse
from .tasks import send_register_email
def first_celery(request):
    email=request.GET.get("email")
    #任务函数的异步调用
    send_register_email.delay(email)
    return HttpResponse("OK")