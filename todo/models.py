from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)  # Заголовок задачи
    description = models.TextField()          # Описание задачи
    due_date = models.DateField()             # Срок выполнения
    status = models.BooleanField(default=False)  # Выполнена или нет

    def __str__(self):
        return self.title
