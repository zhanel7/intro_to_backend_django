from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post

# 📌 Список тем
def thread_list(request):
    threads = Thread.objects.all()
    return render(request, "post/thread_list.html", {"threads": threads})

# 📌 Создание темы
def thread_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        if name and description:
            Thread.objects.create(name=name, description=description)
        return redirect("thread_list")
    return render(request, "post/thread_create.html")

# 📌 Детали темы (и список постов)
def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = thread.posts.all()
    return render(request, "post/thread_detail.html", {"thread": thread, "posts": posts})

# 📌 Удаление темы
def thread_delete(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    thread.delete()
    return redirect("thread_list")

# 📌 Создание поста в теме
def post_create(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        author = request.POST.get("author")
        if title and description and author:
            Post.objects.create(thread=thread, title=title, description=description, author=author)
        return redirect("thread_detail", thread_id=thread.id)
    return render(request, "post/post_create.html", {"thread": thread})

# 📌 Удаление поста
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    thread_id = post.thread.id
    post.delete()
    return redirect("thread_detail", thread_id=thread_id)
