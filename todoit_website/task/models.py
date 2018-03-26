from django.db import models

# Create your models here.
class User(models.Model):
   iD = models.UUIDField(primary_key=True, editable=False)
   name = models.CharField(max_length=128) #temp max length
   email = models.EmailField(max_length=254)

class Project(models.Model):
   iD = models.UUIDField(primary_key=True, editable=False)
   title = models.CharField(max_length=128) #temp max length 
   #description = models.TextField()
   due_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField

class Task(models.Model):
   iD = models.UUIDField(primary_key=True, editable=False)
   title = models.CharField(max_length=128) #temp max length 
   #description = models.TextField()
   do_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField
   due_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField
