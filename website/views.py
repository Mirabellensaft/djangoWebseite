# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import *

# Create your views here.

def post(request):

    contact = Post.objects.get(title__contains='Contact')
    about = Post.objects.get(title__contains='About')
    works = Post.objects.filter(title__contains='Work')#.order_by('published_date')
    return render(request, 'website/post_list.html', {'contact': contact, 'about': about, 'works': works})

#def work(request):
    #work_content = Work.objects.all()
    # work_content = Work.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'website/work.html', {'work_content': work_content})

#def contact(request):
    #contact_content = Contact.objects.all()
    #return render(request, 'website/post_list.html', {'contact_content': contact_content})
