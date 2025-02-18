from django.shortcuts import render, redirect
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm


# Главная страница - перенаправление на /todo-lists
def home_view(request):
	return redirect('todo_lists')


# Список всех TodoLists
def todo_lists_view(request):
	if request.method == 'POST':
		form = TodoListForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo_lists')
	else:
		form = TodoListForm()
	
	todo_lists = TodoList.objects.all()
	return render(request, 'todos/todo_lists.html', {'todo_lists': todo_lists, 'form': form})


# Детали TodoList и задачи в нем
def todo_list_detail_view(request, id):
	todo_list = TodoList.objects.get(id=id)
	todos = Todo.objects.filter(todo_list=todo_list)
	
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.todo_list = todo_list
			todo.save()
			return redirect('todo_list_detail', id=todo_list.id)
	else:
		form = TodoForm()
	
	return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos, 'form': form})


# Удаление TodoList
def todo_list_delete_view(request, id):
	todo_list = TodoList.objects.get(id=id)
	todo_list.delete()
	return redirect('todo_lists')


# Редактирование TodoList
def todo_list_edit_view(request, id):
	todo_list = TodoList.objects.get(id=id)
	if request.method == 'POST':
		form = TodoListForm(request.POST, instance=todo_list)
		if form.is_valid():
			form.save()
			return redirect('todo_list_detail', id=todo_list.id)
	else:
		form = TodoListForm(instance=todo_list)
	
	return render(request, 'todos/todo_list_edit.html', {'form': form})


# Удаление Todo
def todo_delete_view(request, id):
	todo = Todo.objects.get(id=id)
	todo_list_id = todo.todo_list.id
	todo.delete()
	return redirect('todo_list_detail', id=todo_list_id)


# Редактирование Todo
def todo_edit_view(request, id):
	todo = Todo.objects.get(id=id)
	if request.method == 'POST':
		form = TodoForm(request.POST, instance=todo)
		if form.is_valid():
			form.save()
			return redirect('todo_list_detail', id=todo.todo_list.id)
	else:
		form = TodoForm(instance=todo)
	
	return render(request, 'todos/todo_edit.html', {'form': form})
