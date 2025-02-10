from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todos/')
    else:
        form = TodoForm()
    return render(request, 'todo/create_todo.html', {'form': form})

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_delete()
    return redirect('todo_list')
