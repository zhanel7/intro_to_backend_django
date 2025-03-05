from django.db import models

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    seats = models.PositiveIntegerField()
    capacity = models.IntegerField()
    
    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"

