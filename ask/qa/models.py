# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Max
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):

    def new(self):
        return self.last()

    def popular(self):
        return self.objects.all().aggregate(Max('likes'))

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.ImageField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes')

    objects = QuestionManager()

    def __str__(self):
        return self.title

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title