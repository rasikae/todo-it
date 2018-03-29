from django.db import models
import uuid

# Create your models here.
class User(models.Model):
   firstname=models.CharField(max_length=128)
   lastname=models.CharField(max_length=128)
   email=models.EmailField(unique=True,max_length=128)
   username=models.CharField(max_length=128)
   password=models.CharField(max_length=128)

class Project(models.Model):
   title = models.CharField(max_length=128) #temp max length 
   description = models.CharField(max_length=300, default='Add a description')
   due_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField

class Task(models.Model):
   title = models.CharField(max_length=128) #temp max length 
   description = models.CharField(max_length=300, default='Add a description')
   progress = models.CharField(max_length=20,default='Set progress')
   do_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField
   due_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField
