from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return JsonResponse({"posts": list(posts.values())})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return JsonResponse({"post": {"title": post.title, "description": post.description, "author": post.author}})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('/posts/')

# 9. Добавьте маршруты в post/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_create, name='post_create'),
    path('posts/<int:id>/delete/', views.post_delete, name='post_delete'),
]

# 10. Подключите маршруты в cw_2/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
]
