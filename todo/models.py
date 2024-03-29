from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date = models.DateField()
    is_checked = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=Category(name='category_1').pk)
