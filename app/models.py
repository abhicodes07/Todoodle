from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    updation_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} by {self.user}"


class Task(models.Model):
    todo = models.ForeignKey(
        Todo, on_delete=models.CASCADE, related_name="tasks"
    )  # Link tasks to a Todo
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
