from django.db import models
from django.contrib.auth.models import AbstractUser
# from oauth2client.contrib.django_util.models import CredentialsField
import uuid

# import base64
# import pickle

# from django.utils import encoding
# import jsonpickle
# import oauth2client

# Models for User, Tasks, Project

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




# class CredentialsField(models.Field):
#     """Django ORM field for storing OAuth2 Credentials."""

#     def __init__(self, *args, **kwargs):
#         if 'null' not in kwargs:
#             kwargs['null'] = True
#         super(CredentialsField, self).__init__(*args, **kwargs)

#     def get_internal_type(self):
#         return 'BinaryField'

#     def from_db_value(self, value, expression, connection, context):
#         """Overrides ``models.Field`` method. This converts the value
#         returned from the database to an instance of this class.
#         """
#         return self.to_python(value)

#     def to_python(self, value):
#         """Overrides ``models.Field`` method. This is used to convert
#         bytes (from serialization etc) to an instance of this class"""
#         if value is None:
#             return None
#         elif isinstance(value, oauth2client.client.Credentials):
#             return value
#         else:
#             try:
#                 return jsonpickle.decode(
#                     base64.b64decode(encoding.smart_bytes(value)).decode())
#             except ValueError:
#                 return pickle.loads(
#                     base64.b64decode(encoding.smart_bytes(value)))

#     def get_prep_value(self, value):
#         """Overrides ``models.Field`` method. This is used to convert
#         the value from an instances of this class to bytes that can be
#         inserted into the database.
#         """
#         if value is None:
#             return None
#         else:
#             return encoding.smart_text(
#                 base64.b64encode(jsonpickle.encode(value).encode()))

#     def value_to_string(self, obj):
#         """Convert the field value from the provided model to a string.

#         Used during model serialization.

#         Args:
#             obj: db.Model, model object

#         Returns:
#             string, the serialized field value
#         """
#         value = self._get_val_from_obj(obj)
#         return self.get_prep_value(value)

# class Credentials(models.Model):
#     iD = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     credential = CredentialsField()