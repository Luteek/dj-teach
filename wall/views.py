from django.shortcuts import render
from .models import Post

# Create your views here.

def wall(request):
    post = Post.objects.order_by('pub_date')
    return render(request, 'wall/wall.html', {'posts': post})