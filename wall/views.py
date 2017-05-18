from django.utils import timezone

from django.shortcuts import render, redirect
from .models import Post
from .forms import PostFrom

# Create your views here.

def wall(request):
    post = Post.objects.order_by('pub_date')
    return render(request, 'wall/wall.html', {'posts': post})

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

