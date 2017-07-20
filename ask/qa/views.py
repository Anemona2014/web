# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.views import generic
from .models import Question

# Create your views here.


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def error(request, *arg, **kwargs):
    raise Http404()


class QuestionListView(generic.ListView):
    model = Question
    template_name = '/home/anemona/box/web/ask/templates/question_list.html'
    paginate_by = 1

    def get_queryset(self):
        return Question.objects.new()