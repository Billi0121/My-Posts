from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import CreateView

# Create your views here.
def index(request):
    model = post
    form = PostsForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'posts/index.html', {'form': form})

def success(request):
    return render(request, 'posts/success.html')

def edit_post(request, post_id):
    posts = post.objects.get(pk=post_id)
    form = PostsForm(
        request.POST or None,
        instance=posts
        ) 
    if form.is_valid():
        form.save()
    return render(request, 'posts/index.html', {'form': form}) 