#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 10:57
# @Author  : Meng
# @File    : celery.py
# @Software: PyCharm
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# 这是wsgi.py中的数据copy下，配置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_v1.settings')
app = Celery('django_v1')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))