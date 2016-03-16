from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=0)
    order = models.IntegerField(null=True)
