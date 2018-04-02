from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import taskform
from .forms import projectform
from .forms import registerform
from .forms import loginform
from django.utils import timezone
from .forms import subtaskform
from .models import Task
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import login_required
from .models import Project
# Create your views here.

def login(request):
    print("login function")

    # User.objects.all().delete() # deletes all users in database

    if request.method == 'POST':
      if 'loginbutton' in request.POST:
      	print("'loginbutton' found")
      	loginform_req = loginform(request.POST)

      	if loginform_req.is_valid():
	        username = loginform_req.cleaned_data['username']
	        password = loginform_req.cleaned_data['password']

       		print(password)

	        user = authenticate(username=username,password=password)

	        print(user)
	        
	        if user is not None:
	        	print("user is not none")
	        	if user.is_active:
	        		auth_login(request,user)
	        		messages.success(request,username)
	        		return HttpResponseRedirect('home')
                
      elif 'registerbutton' in request.POST:
          print("'registerbutton' found")
          registerform_req = registerform(request.POST)
          if registerform_req.is_valid():
              newuser = User(email = registerform_req.cleaned_data['email'])
              newuser.first_name = registerform_req.cleaned_data['firstname']
              newuser.last_name = registerform_req.cleaned_data['lastname']
              newuser.username = registerform_req.cleaned_data['username']
              newuser.password = registerform_req.cleaned_data['password']

              newuser.set_password(registerform_req.cleaned_data['password'])
              
              print("User created but not saved")
              
              newuser.last_login = timezone.now()
              newuser.save()

              print("User saved")

              messages.success(request,newuser.email)

              # simpling doing this does the same as below..?
              # return HttpResponseRedirect('home')

              form = taskform()
              form2 = projectform()
              form3 = subtaskform()

              tasks = Task.objects.all()
              projects = Project.objects.all()
              users = User.objects.all()

              return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2,"form3":form3})
          
    cform = registerform()
    lform = loginform()

    return render(request,'task/login.html',{"registerform":cform,"loginform":lform})


@login_required
def home(request):
	# Task.objects.all().delete() # deletes all task objects

  # if this is a POST request we need to process the form data
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    if 'tasksubmit' in request.POST:
      form = taskform(request.POST)
      form2 = projectform()
      form3 = subtaskform()

      # check whether it's valid:
      if form.is_valid():
        # process the data in form.cleaned_data as required        
        newtask = Task(title = form.cleaned_data['title'])
        newtask.do_date = form.cleaned_data['dodate']
        newtask.due_date = form.cleaned_data['duedate']
        newtask.progress = form.cleaned_data['progress']
        newtask.description = form.cleaned_data['description']

        newtask.save()
        
        tasks = Task.objects.all()
        projects = Project.objects.all()
        users = User.objects.all()
        form = taskform()

        # redirect to a new URL:
        return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2,"form3":form3})
    
    elif 'projectsubmit' in request.POST:
      form = taskform()
      form2 = projectform(request.POST)
      form3 = subtaskform()

      # check whether it's valid:
      if form2.is_valid():
        # process the data in form.cleaned_data as required
        newpro = Project(title = form2.cleaned_data['title'])
        newpro.due_date = form2.cleaned_data['duedate']

        newpro.save()
        
        tasks = Task.objects.all()
        projects = Project.objects.all()
        users = User.objects.all()
        form2 = projectform()

        # redirect to a new URL:
        return render(request, 'task/home.html', {'users':users,'tasks':tasks,'projects':projects,'form': form, 'form2':form2,"form3":form3})
    
    elif 'subtasksubmit' in request.POST:
      form = taskform()
      form2 = projectform()
      form3 = subtaskform(request.POST)

      if form3.is_valid():
        tasks = Task.objects.all()
        projects = Project.objects.all()
        users = User.objects.all()
        form3 = subtaskform()

        return render(request, 'task/home.html', {'users':users,'tasks':tasks,'projects':projects,'form': form, 'form2':form2, "form3":form3})
          
  form = taskform()
  form2 = projectform()
  form3 = subtaskform()

  tasks = Task.objects.all()
  projects = Project.objects.all()
  users = User.objects.all()

  return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2, "form3":form3})


#pbkdf2_sha256$100000$twFZOefwKMsn$Q19ITpa+fyzEW0R0q/vOyJtAdIwkMrowVSKJK74K/5Q=
#pbkdf2_sha256$100000$urrwW070p6dB$1KQkbZHEVVKMDK82UjDdvZgnzN8LY1y/jmODU9S+FNQ=