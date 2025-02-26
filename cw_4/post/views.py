from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def redirect_to_threads(request):
    return redirect('threads_list')


def threads_list(request):
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('threads_list')  # Перенаправляем после успешного добавления
    else:
        form = ThreadForm()
    
    threads = Thread.objects.all()
    return render(request, 'post/threads_list.html', {'threads': threads, 'form': form})


def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # Учтем файлы (картинки)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread  # Привязываем пост к текущему треду
            post.save()
            return redirect('thread_detail', id=thread.id)  # Перезагрузка страницы

    else:
        form = PostForm()  # Обычная форма для GET-запроса

    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})


def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('threads_list')

def thread_edit(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('threads_list')
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'post/thread_edit.html', {'form': form})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_edit.html', {'form': form})

