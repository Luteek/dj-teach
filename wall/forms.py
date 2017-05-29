from django import forms
from .models import  Post, PostPartial, General, Classes, Parents, Colleagues

class PostFrom(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('caption', 'content', 'image', )

class PostPartialForm(forms.ModelForm):

    class Meta:
        model = PostPartial
        fields = ('caption', 'content',)



## All forms for models

class GeneralPost(forms.ModelForm):
    class Meta:
        model = General
        fields = ('caption', 'content',)


class ClassesPost(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ('caption', 'content',)


class ParentsPost(forms.ModelForm):
    class Meta:
        model = Parents
        fields = ('caption', 'content',)


class ColleaguesPost(forms.ModelForm):
    class Meta:
        model = Colleagues
        fields = ('caption', 'content',)

