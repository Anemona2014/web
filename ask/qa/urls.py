
# -*- coding: utf-8 -*-
__author__ = 'menkovich'
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.QuestionListView.as_view(), name='question'),
    url(r'^question/(\d+)/$', views.test),
    url(r'^login/.*$', views.test),
    url(r'^signup/.*$', views.test),
    url(r'^ask/.*$', views.test),
    url(r'^popular/.*$', views.test),
    url(r'^new/.*$', views.test),
]
