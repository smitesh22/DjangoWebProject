from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image,Audio

class ImageForms(forms.ModelForm):
    title = forms.CharField(label = 'title',max_length=100)
    image = forms.ImageField(label ='file')
    class Meta:
        model = Image
        fields =['title','image']

class AudioForms(forms.ModelForm):
    title = forms.CharField(label = 'title',max_length=100)
    file = forms.FileField(label ='file')
    class Meta:
        model = Audio
        fields =['title','file']

