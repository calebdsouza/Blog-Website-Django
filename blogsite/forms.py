from django import forms
from django.forms import ModelForm, TextInput, Textarea

from .models import Post

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
                    'title': TextInput(attrs={'class': 'form-title-input'}),
                    'text': Textarea(attrs={'class': "form-text-input"}),
                    }
        