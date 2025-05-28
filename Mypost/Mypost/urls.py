"""
URL configuration for Mypost project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Here I'm talking about what i did or doing.Working with sites what i shoul do what to learn and how is My days go

from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts'))
    # path('', views.index, name='index'),
    # path('success/', views.success, name='success'),
    # path('posts/', views.posts, name='posts'),
    # path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
]
