from django.shortcuts import render

# Create your views here.

def wall(request):
    return render(request, 'wall/wall.html')