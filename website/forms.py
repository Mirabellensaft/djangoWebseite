from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Post, Admin
from .helperfunctions import randomnumber

class DisplayPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image', 'url1', 'number')
        image = forms.ImageField(
            label='select an image file'
        )

class Admin(forms.ModelForm):

    class Meta:
        model = Admin
        fields = ('title', 'text', 'url1', 'url2', 'url3', 'email', 'phone', 'location'
        )
        resume = forms.FileField(
            label='select a file'
        )



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

f = DisplayPost()
f.as_p()
print (randomnumber())
print (f.as_p())
