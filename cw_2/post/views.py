from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

# Получение всех постов
def post_list(request):
    posts = list(Post.objects.values())
    return JsonResponse(posts, safe=False, json_dumps_params={'ensure_ascii': False})

# Получение одного поста по ID
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return JsonResponse(
        {"title": post.title, "description": post.description, "author": post.author},
        json_dumps_params={'ensure_ascii': False}
    )

# Создание поста
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Post created successfully!"}, status=201)
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})

# Удаление поста
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('/todos')  # Перенаправление после удаления
