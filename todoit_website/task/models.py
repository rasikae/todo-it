from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

# model used to represent a User class object
class User(AbstractUser):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField(unique=True, max_length=128)
    username = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=128)
    collab = models.CharField(default="", max_length=250)

# model used to represent a Project class object
class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=300, default='Add a description')
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    parent = models.CharField(max_length=128, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

# model used to represent a Task/subtask class object
class Task(models.Model):
    title = models.CharField(max_length=128)  # temp max length
    description = models.CharField(max_length=300, default='Add a description')
    progress = models.CharField(max_length=20, default='Set progress')
    do_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_sub = models.BooleanField(default=False)
    parent = models.CharField(max_length=128, null=True)
    project = models.CharField(max_length=128, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
