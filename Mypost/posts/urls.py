from django.urls import path
from . import views

app_name = 'posts'


urlpatterns = [
    path('api/v1/posts/<int:pk>/', views.get_post, name='PostView'),
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('posts/', views.posts, name='posts'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
]
