from django.db import models
import uuid

# Create your models here.
class User(models.Model):
   # uID = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
   # iD = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
   name = models.CharField(max_length=128) #temp max length
   email = models.EmailField(unique=True, max_length=254)
   #password=models.CharField(max_length=128)

class Project(models.Model):
   # pID=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
   # iD = models.UUIDField(editable=False, default=uuid.uuid4)
   title = models.CharField(max_length=128) #temp max length 
   description = models.CharField(max_length=300, default='Add a description')
   due_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField

class Task(models.Model):
   # tID=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
   # iD = models.UUIDField(editable=False, default=uuid.uuid4)
   title = models.CharField(max_length=128) #temp max length 
   description = models.CharField(max_length=300, default='Add a description')
   progress = models.CharField(max_length=20,default='Set progress')
   do_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField
   due_date = models.DateTimeField(auto_now=False,auto_now_add=False) #can also be just DateField
