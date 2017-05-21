from django.utils import timezone

from django.shortcuts import render, redirect
from .models import Post, PostPartial
from .forms import PostFrom, PostPartialForm

# Create your views here.


def wall(request):
    """отображает нам все посты"""
    # -pub_date сортирует по дате список постов. Новые вверху
    post = Post.objects.order_by('-pub_date')
    return render(request, 'wall/wall.html', {'posts': post})

def partial(request):
    post = PostPartial.objects.order_by('-pub_date')
    return render(request, 'wall/partial.html', {'posts': post})

def post_new(request):
    if request.method == "POST":
        form = PostFrom(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/wall/')
        else:
            return render(request, 'wall/post_edit.html', {'form': form})
    else:
        form = PostFrom()
        return render(request, 'wall/post_edit.html', {'form': form})


def postPartial_new(request):
    if request.method == "POST":
        form = PostPartialForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return  redirect('/wall/partial.html')
        else:
            return  render(request, 'wall/post_partial_edit.html', {'form': form})
    else:
        form = PostPartialForm()
        return  render(request, 'wall/post_partial_edit.html', {'form': form})
