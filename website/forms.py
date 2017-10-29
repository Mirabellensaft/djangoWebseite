from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Post

class DisplayPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')
        image = forms.ImageField(
            label='select an image file'
        )

class EditContact(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

f = DisplayPost()
f.as_p()
print f.as_p()
