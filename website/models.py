# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone




# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Description')
    image = models.ImageField(upload_to='img', height_field=None, width_field=None)
    number = models.IntegerField(default = 0)
    url1 = models.URLField(default='URL')
    url1text = models.CharField(default='URL', max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank = True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Admin(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Description')
    resume = models.FileField(upload_to=' ')
    location = models.CharField(default='Berlin', max_length=200)
    phone = models.CharField(default='Your number', max_length=200)
    email = models.EmailField(default='Your mail')
    url1 = models.URLField(default='URL')
    url1text = models.CharField(default='URL', max_length=200)
    url2 = models.URLField(default='URL')
    url2text = models.CharField(default='URL', max_length=200)
    url3 = models.URLField(default='URL')
    url3text = models.CharField(default='URL', max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank = True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
