# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    display_title = models.CharField(max_length=200, default='SOME STRING')
    title = models.CharField(max_length=200)
    text = models.TextField()
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    mail = models.EmailField(max_length=254)
    image = models.ImageField(upload_to='img', height_field=None, width_field=None, default='SOME STRING')
    number = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank = True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
