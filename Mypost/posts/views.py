from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.http import JsonResponse
from serializers import PostSerializer

# Create your views here.
def index(request):
    model = post
    form = PostsForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'posts/index.html', {'form': form})

def success(request):
    return render(request, 'posts/success.html')

def posts(request):
    posts = post.objects.get(pk=3)
    return render(request, 'posts/allposts.html', {'post': posts})

def edit_post(request, post_id):
    posts = post.objects.get(pk=post_id)
    form = PostsForm(
        request.POST or None,
        instance=posts
         ) 
    if form.is_valid():
        form.save()
        return redirect('success')
    return render(request, 'posts/index.html', {'form': form}) 

def get_post(request, post_id):
    if request.method == 'GET':
        post = post.objects.get(pk=post_id)
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)
