from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
   firstname = models.CharField(max_length=128)
   lastname = models.CharField(max_length=128)
   email = models.EmailField(unique=True,max_length=128)
   username = models.CharField(unique=True,max_length=128)
   password = models.CharField(max_length=128)
class Project(models.Model):
   title = models.CharField(max_length=128) #temp max length 
   description = models.CharField(max_length=300, default='Add a description')
   due_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField
   relates_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Task(models.Model):
   title = models.CharField(max_length=128) #temp max length 
   description = models.CharField(max_length=300, default='Add a description')
   progress = models.CharField(max_length=20,default='Set progress')
   do_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField
   due_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField
   is_sub = models.BooleanField(default=False)
   relates_to = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
