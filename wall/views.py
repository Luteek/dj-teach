from django.utils import timezone

from django.shortcuts import render, redirect
from .models import Post, PostPartial, General, Classes, Colleagues, Parents
from .forms import PostFrom, PostPartialForm, GeneralPost,  ClassesPost, ParentsPost, ColleaguesPost

# Create your views here.
def general(request):
    post = General.objects.order_by('-pub_date')
    return render(request, 'wall/general.html', {'posts': post})

def classes(request):
    post = Classes.objects.order_by('-pub_date')
    return render(request, 'wall/class.html', {'posts': post})

def parent(request):
    post = Parents.objects.order_by('-pub_date')
    return render(request, 'wall/parents.html', {'posts': post})

def colleagues(request):
    post = Colleagues.objects.order_by('-pub_date')
    return render(request, 'wall/colleagues.html', {'posts': post})


## NEW POSTS

def new_postGeneral(request):
    if request.method == "POST":
        form = GeneralPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/wall/')
        else:
            return render(request, 'wall/new_post/new_general.html', {'form': form})
    else:
        form = GeneralPost()
        return render(request, 'wall/new_post/new_general.html', {'form': form})

def new_postClasses(request):
    if request.method == "POST":
        form = ClassesPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/wall/class')
        else:
            return render(request, 'wall/new_post/new_class.html', {'form': form})
    else:
        form = ClassesPost()
        return render(request, 'wall/new_post/new_class.html', {'form': form})

def new_postParents(request):
    if request.method == "POST":
        form = ParentsPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/wall/parents')
        else:
            return render(request, 'wall/new_post/new_parents.html', {'form': form})
    else:
        form = ParentsPost()
        return render(request, 'wall/new_post/new_parents.html', {'form': form})

def new_postColleagues(request):
    if request.method == "POST":
        form = ColleaguesPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('/wall/colleagues')
        else:
            return render(request, 'wall/new_post/new_colleg.html', {'form': form})
    else:
        form = ColleaguesPost()
        return render(request, 'wall/new_post/new_colleg.html', {'form': form})

# POSTS IN NEW PAGE of ID
def postGeneral(request, type, ident):
    if type == '1':
        post = General.objects.get(id=ident)
    elif type =='2':
        post = Classes.objects.get(id=ident)
    elif type == '3':
        post = Parents.objects.get(id=ident)
    elif type == '4':
        post = Colleagues.objects.get(id=ident)
    return render(request, 'wall/post.html', {"post": post})



# EDIT POSTS








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
