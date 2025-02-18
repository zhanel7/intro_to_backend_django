from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Форма для создания и редактирования Todo
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

# HTML-страница со списком Todo
def todo_list_view(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

# API для получения списка и создания Todo
class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# API для получения одной Todo по ID
class TodoDetailView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Создание новой Todo через форму
def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

# Удаление Todo и редирект на список
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')
