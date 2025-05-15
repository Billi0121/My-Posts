from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import CreateView

# Create your views here.
class index(CreateView):
    form_class = PostsForm
    template_name = 'posts/index.html'
    success_url = 'success'

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