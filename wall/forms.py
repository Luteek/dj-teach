from django import forms
from .models import  Post, PostPartial

class PostFrom(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('caption', 'content', 'image', )


class PostPartialForm(forms.ModelForm):

    class Meta:
        model = PostPartial
        fields = ('caption', 'content',)