#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 11:29
# @Author  : Meng
# @File    : tasks.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django_v1 import settings
from django.core.mail import send_mail

@shared_task
def send_register_email(email):
    message = ''
    title = '甲骨文的信息'
    body = '<h1>大家好，欢迎成为甲骨文IT的精英</h1>'
    try:
        send_mail(title, message, settings.EMAIL_HOST_USER, [email], html_message=body)
    except Exception as e:
        print(e)