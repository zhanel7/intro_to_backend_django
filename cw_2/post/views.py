from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post/post_detail.html', {'post': post})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')
