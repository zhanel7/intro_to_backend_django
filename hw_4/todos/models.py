from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    todo_list = models.ForeignKey(TodoList, related_name='todos', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
