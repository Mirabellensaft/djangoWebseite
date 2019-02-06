# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post as Post_model
from .models import Admin as Admin_model
from .forms import DisplayPost, ContactForm, Admin
from .helperfunctions import randomnumber


# Create your views here.

def post(request):
    admin = Admin_model.objects.get(title='Admin')
    works = Post_model.objects.filter(title__contains=' ')#.order_by('published_date')
    return render(request, 'website/post_list.html', {'admin': admin, 'works': works})
    # return render(request, 'website/post_list.html', {'works': works})

@login_required
def admin_page(request, pk):

    post = get_object_or_404(Post_model.objects, pk=pk)
    if request.method == "POST":
        form = Admin_model(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = Admin_model(instance=post)
    print (form.as_p())
    return render(request, 'website/admin_page.html', {'form': form})


def work_detail(request, pk):

    work = get_object_or_404(Post_model, pk=pk)
    return render(request, 'website/work_detail.html', {'work': work})

@login_required
def displayPost_new(request):

    if request.method == "POST":
        form = DisplayPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            post.published_date = timezone.now()
            post.number = randomnumber()
            post = Post(image = request.FILES['image'])
            post.save()
            return redirect('post_list')
    else:
        form = DisplayPost()
    print (form.as_p())
    return render(request, 'website/display_edit.html', {'form': form})

@login_required
def display_edit(request, pk):

    post = get_object_or_404(Post_model, pk=pk)
    if request.method == "POST":
        form = DisplayPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post = Post_model(image = request.FILES['image'])
            post.save()
            return redirect('work_detail', pk=post.pk)
    else:
        form = DisplayPost(instance=post)
    print (form.as_p())
    return render(request, 'website/display_edit.html', {'form': form})


def sendMail(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients =['tanja@transfeld.net']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients, name)
            return redirect('post_list')
    else:
        form = ContactForm()
        return render(request, 'website/post_list.html', {'form': form})
            #return HttpResponseRedirect('/thanks/')
            #idee: alternative post_list seite mit inaktivem formular,mit danke

#def work(request):
    #work_content = Work.objects.all()
    # work_content = Work.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'website/work.html', {'work_content': work_content})

#def contact(request):
    #contact_content = Contact.objects.all()
    #return render(request, 'website/post_list.html', {'contact_content': contact_content})
