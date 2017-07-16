# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def error(request, *arg, **kwargs):
    raise Http404()
