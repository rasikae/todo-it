from .models import Task
from .models import User
from .models import Project
from .forms import taskform
from .forms import projectform
from .forms import registerform
from .forms import loginform
from .forms import collabform
from .forms import subtaskform
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from datetime import timedelta
import datetime
import os
import operator

# Login View manages login and registration
def login(request):
    print("login function")
    
    # User.objects.all().delete() # deletes all users in database

 		# If user is trying to login, check and authenticate user
    if request.method == 'POST':
        # If login form is submitted
        if 'loginbutton' in request.POST:
            print("'loginbutton' found")
            loginform_req = loginform(request.POST)
            
            if loginform_req.is_valid():
                username = loginform_req.cleaned_data['username']
                password = loginform_req.cleaned_data['password']

                user = authenticate(username=username, password=password)

                print(user)

                #If login form contained correct user info then sign in and redirect to home
                if user is not None:
                    print("user is not none")
                    if user.is_active:
                    		auth_login(request,user)
                    		messages.success(request, username)
                    		return redirect('home')
        # If register form is submitted
        elif 'registerbutton' in request.POST:
            print("'registerbutton' found")
            registerform_req = registerform(request.POST)

            if registerform_req.is_valid():
                newuser = User(email=registerform_req.cleaned_data['email'])
                newuser.first_name = registerform_req.cleaned_data['firstname']
                newuser.last_name = registerform_req.cleaned_data['lastname']
                newuser.username = registerform_req.cleaned_data['username']
                newuser.password = registerform_req.cleaned_data['password']
                newuser.collab = ""
                newuser.set_password(registerform_req.cleaned_data['password'])

                print("User created but not saved")
                
                # Create new user with form info
                
                newuser.last_login = timezone.now()
                newuser.save()

                print("User saved")

                # simpling doing this does the same as below..?
                # return redirect('home')

                # Sets context to send in render
                date = datetime.date.today()
                start_week = date - datetime.timedelta(date.weekday())
                end_week = start_week + datetime.timedelta(7)
                form = taskform()
                form2 = projectform()
                form3 = subtaskform()
                form4 = collabform()

                username = registerform_req.cleaned_data['username']
                password = registerform_req.cleaned_data['password']
                user = authenticate(username=username, password=password)

                #Authenticate suser and redirects to home page
                if user is not None:
                    if user.is_active:
                        auth_login(request,user)
                        messages.success(request, username)
                        weekly = Task.objects.filter(
                            due_date__range=[start_week, end_week])
                        daily = Task.objects.filter(
                            due_date__date=datetime.date.today())
                        tasks = Task.objects.all().filter(user=request.user)
                        projects = Project.objects.all().filter(user=request.user)
                        collabs = request.user.collab.replace(
                            ' ', '').split(',')
                        users1 = User.objects.filter(username__in=collabs)
                        users = Task.objects.filter(user__in=users1)
                        return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, "form4": form4, "currentproject": "", "weekly": weekly, "daily": daily})

    cform = registerform()
    lform = loginform()
    #If failed to log in then reload login page
    return render(request, 'task/login.html', {"registerform": cform, "loginform": lform})


@login_required
def home(request, delete=''):
	  # Task.objects.all().delete() # deletes all task objects
	  
	  # Sets context to send in render
	  date = datetime.date.today()
	  start_week = date - datetime.timedelta(date.weekday())
	  end_week = start_week + datetime.timedelta(7)
	  form = taskform()
	  form2 = projectform()
	  form3 = subtaskform()
	  form4 = collabform()
	  weekly = Task.objects.filter(due_date__range=[start_week, end_week])
	  daily = Task.objects.filter(due_date__date=datetime.date.today())
	  tasks = Task.objects.all().filter(user=request.user)
	  projects = Project.objects.all().filter(user=request.user)
	  collabs = request.user.collab.replace(' ', '').split(',')
	  users1 = User.objects.filter(username__in=collabs)
	  users = Task.objects.filter(user__in=users1)
	  weekly=""
	  daily=""
	  
	  # if this is a GET request then it is a delete task request
	  if request.method == 'GET':
	      Task.objects.filter(title=request.GET.get('delete', False))
	      weekly = Task.objects.filter(due_date__range=[start_week, end_week])
	      daily = Task.objects.filter(due_date__date=datetime.date.today())
	      tasks = Task.objects.all().filter(user=request.user)
	      form = taskform()
	      return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})
	  
	   # if this is a POST request we need to figure out which one
	  if request.method == 'POST':
	      # The following are different sort requests, sorting is done, then the page is refreshed
	      if "sortadded" in request.POST:
	          tasks = Task.objects.all().filter(user=request.user)
	          users = Task.objects.filter(user__in=users1)
	          return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})                
	      if "sorttitle" in request.POST:
	          tasks = Task.objects.all().filter(user=request.user).order_by('title')
	          users = Task.objects.filter(user__in=users1).order_by('title')
	          return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})                
	      if "sortdo" in request.POST:
	          tasks = Task.objects.all().filter(user=request.user).order_by('do_date')
	          users = Task.objects.filter(user__in=users1).order_by('do_date')
	          return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})                
	      if "sortdue" in request.POST:
	          tasks = Task.objects.all().filter(user=request.user).order_by('due_date')
	          users = Task.objects.filter(user__in=users1).order_by('due_date')
	          return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})                
	      if "sortweek" in request.POST:
	          weekly="Yes"
	          tasks = Task.objects.filter(user=request.user, due_date__range=[start_week, end_week])
	          users = Task.objects.filter(user__in=users1).order_by('due_date')
	          return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})                
	      if "sortday" in request.POST:
	          daily="Yes"
	          tasks = Task.objects.filter(user=request.user, due_date__date=datetime.date.today())
	          users = Task.objects.filter(user__in=users1).order_by('due_date')
	          return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})                
	         
	      # the following are various submit forms
	      
	      # takes new task form data and creates a new task
	      if 'tasksubmit' in request.POST:
	          form = taskform(request.POST)
	          # check whether it's valid:
	          if form.is_valid():
	                  # process the data in form.cleaned_data as required
	                  # ...
	                  # redirect to a new URL:
	              newtask = Task(title=form.cleaned_data['title'])
	              newtask.do_date = form.cleaned_data['dodate']
	              newtask.due_date = form.cleaned_data['duedate']
	              newtask.progress = form.cleaned_data['progress']
	              newtask.description = form.cleaned_data['description']
	              newtask.project = form.cleaned_data['project']
	              newtask.is_sub = False
	              newtask.user = request.user
	              newtask.save()
	              weekly = Task.objects.filter(
	                  due_date__range=[start_week, end_week])
	              daily = Task.objects.filter(
	                  due_date__date=datetime.date.today())
	              tasks = Task.objects.all().filter(user=request.user)
	              form = taskform()
	              for x in tasks: 
	                print(x)
	              print("Hello")
	              return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})
	      
	      # reads same type of form as above, modifies fields for given title
	      if 'taskedit' in request.POST:
	          form = taskform(request.POST)
	          # check whether it's valid:
	          if form.is_valid():
	              # process the data in form.cleaned_data as required
	              # ...
	              # redirect to a new URL:
	              try:
	                  task = Task.objects.get(title=form.cleaned_data['title'], user=request.user)
	              except ObjectDoesNotExist:
	                  task = None
	              if task:
	                  task.do_date = form.cleaned_data['dodate']
	                  task.due_date = form.cleaned_data['duedate']
	                  task.progress = form.cleaned_data['progress']
	                  task.description = form.cleaned_data['description']
	                  task.project = form.cleaned_data['project']
	                  task.is_sub = False
	                  task.user = request.user
	                  task.save()
	                  weekly = Task.objects.filter(
	                      due_date__range=[start_week, end_week])
	                  daily = Task.objects.filter(
	                      due_date__date=datetime.date.today())
	                  tasks = Task.objects.all().filter(user=request.user)
	                  form = taskform()
	                  return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})
          
         # Adds current user to given user's collaborators
	      if 'collabsubmit' in request.POST:
	          form4 = collabform(request.POST)
	          print("adding collaborator")
	          # check whether it's valid:
	          if form4.is_valid():
	              # process the data in form.cleaned_data as required
	              # ...
	              # redirect to a new URL:
	              collabname = form4.cleaned_data['name']
	              try:
	                  temp_user = User.objects.get(username=collabname)
	              except ObjectDoesNotExist:
	                  temp_user = None
	              if temp_user:
	                  temp_user.collab = temp_user.collab+","+request.user.username
	                  temp_user.save()
	                  collabs = request.user.collab.replace(' ', '').split(',')
	                  users1 = User.objects.filter(username__in=collabs)
	                  users = Task.objects.filter(user__in=users1)
	                  form4 = collabform()
	                  return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})
          
          # Creates new project from form data
	      elif 'projectsubmit' in request.POST:
	          form2 = projectform(request.POST)
	          # check whether it's valid:
	          if form2.is_valid():
	              # process the data in form.cleaned_data as required
	              # ...
	              # redirect to a new URL:
	              newpro = Project(title=form2.cleaned_data['title'])
	              newpro.due_date = form2.cleaned_data['duedate']
	              newpro.parent = form2.cleaned_data['parent']
	              newpro.user = request.user
	              newpro.save()
	              projects = Project.objects.all().filter(user=request.user)
	              form2 = projectform()
	              return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})
	      
	      # Creates subtask for given task with form info
	      elif 'subtasksubmit' in request.POST:
	          form3 = subtaskform(request.POST)
	          if form3.is_valid():
	              newtask = Task(title=form3.cleaned_data['title'])
	              newtask.do_date = form3.cleaned_data['dodate']
	              newtask.due_date = form3.cleaned_data['duedate']
	              newtask.progress = form3.cleaned_data['progress']
	              newtask.description = form3.cleaned_data['description']
	              newtask.project = form3.cleaned_data['project']
	              newtask.parent = form3.cleaned_data['parent']
	              newtask.is_sub = True
	              newtask.user = request.user
	              newtask.save()
	              weekly = Task.objects.filter(
	                  due_date__range=[start_week, end_week])
	              daily = Task.objects.filter(
	                  due_date__date=datetime.date.today())
	              tasks = Task.objects.all().filter(user=request.user)
	              form3 = subtaskform()
	              return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})
	      elif 'logoutbutton' in request.POST:
	      	print("logging out")
	      	auth_logout(request)
	      	return redirect('login')
	  return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})                

def home2(request, project):
    # This view is for projects, is largely the same as the home view
    
    # Task.objects.all().delete() # deletes all task objects
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    form = taskform()
    form2 = projectform()
    form3 = subtaskform()
    form4 = collabform()
    weekly = Task.objects.filter(due_date__range=[start_week, end_week])
    daily = Task.objects.filter(due_date__date=datetime.date.today())
    tasks = Task.objects.all().filter(user=request.user)
    projects = Project.objects.all().filter(user=request.user)
    collabs = request.user.collab.replace(' ', '').split(',')
    users1 = User.objects.filter(username__in=collabs)
    users = Task.objects.filter(user__in=users1)
    weekly=""
    daily=""
    
    if request.method == 'GET':
        # Decides if the get request is for a task delete, or to view a project
        if '/' in project:
            task = os.path.basename(project)
            Task.objects.filter(title=task).delete()
            weekly = Task.objects.filter(
                due_date__range=[start_week, end_week])
            daily = Task.objects.filter(due_date__date=datetime.date.today())
            tasks = Task.objects.all().filter(user=request.user)
            return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})
        elif not project:
            return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": "", "weekly": weekly, "daily": daily})
        else:
            return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})

    if request.method == 'POST':
        if "sortadded" in request.POST:
            tasks = Task.objects.all().filter(user=request.user)
            users = Task.objects.filter(user__in=users1)
            return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})                
        if "sorttitle" in request.POST:
            tasks = Task.objects.all().filter(user=request.user).order_by('title')
            users = Task.objects.filter(user__in=users1).order_by('title')
            return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})                
        if "sortdo" in request.POST:
            tasks = Task.objects.all().filter(user=request.user).order_by('do_date')
            users = Task.objects.filter(user__in=users1).order_by('do_date')
            return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})                
        if "sortdue" in request.POST:
            tasks = Task.objects.all().filter(user=request.user).order_by('due_date')
            users = Task.objects.filter(user__in=users1).order_by('due_date')
            return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})                
        if "sortweek" in request.POST:
            weekly="Yes"
            tasks = Task.objects.filter(user=request.user, due_date__range=[start_week, end_week])
            users = Task.objects.filter(user__in=users1).order_by('due_date')
            return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})                
        if "sortday" in request.POST:
            daily="Yes"
            tasks = Task.objects.filter(user=request.user, due_date__date=datetime.date.today())
            users = Task.objects.filter(user__in=users1).order_by('due_date')
            return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})                

        # create a form instance and populate it with data from the request:
        if 'tasksubmit' in request.POST:
            form = taskform(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                newtask = Task(title=form.cleaned_data['title'])
                newtask.do_date = form.cleaned_data['dodate']
                newtask.due_date = form.cleaned_data['duedate']
                newtask.progress = form.cleaned_data['progress']
                newtask.description = form.cleaned_data['description']
                newtask.project = form.cleaned_data['project']
                newtask.is_sub = False
                newtask.user = request.user
                newtask.save()
                weekly = Task.objects.filter(
                    due_date__range=[start_week, end_week])
                daily = Task.objects.filter(
                    due_date__date=datetime.date.today())
                tasks = Task.objects.all().filter(user=request.user)
                form = taskform()
                return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})
        if 'taskedit' in request.POST:
            form = taskform(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                try:
                    task = Task.objects.get(title=form.cleaned_data['title'])
                except ObjectDoesNotExist:
                    task = None
                if task:
                    task.do_date = form.cleaned_data['dodate']
                    task.due_date = form.cleaned_data['duedate']
                    task.progress = form.cleaned_data['progress']
                    task.description = form.cleaned_data['description']
                    task.project = form.cleaned_data['project']
                    task.is_sub = False
                    task.user = request.user
                    task.save()
                    weekly = Task.objects.filter(
                        due_date__range=[start_week, end_week])
                    daily = Task.objects.filter(
                        due_date__date=datetime.date.today())
                    tasks = Task.objects.all().filter(user=request.user)
                    form = taskform()
                    return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})

        if 'collabsubmit' in request.POST:
            form4 = collabform(request.POST)
            # check whether it's valid:
            if form4.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                collabname = form4.cleaned_data['name']
                try:
                    temp_user = User.objects.get(username=collabname)
                except ObjectDoesNotExist:
                    temp_user = None
                if temp_user:
                    temp_user.collab = temp_user.collab+","+request.user.username
                    temp_user.save()
                    collabs = request.user.collab.replace(' ', '').split(',')
                    users1 = User.objects.filter(username__in=collabs)
                    users = Task.objects.filter(user__in=users1)
                    form4 = collabform()
                    return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})

        elif 'projectsubmit' in request.POST:
            form2 = projectform(request.POST)
            # check whether it's valid:
            if form2.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                newpro = Project(title=form2.cleaned_data['title'])
                newpro.due_date = form2.cleaned_data['duedate']
                newpro.parent = form2.cleaned_data['parent']
                newpro.user = request.user
                newpro.save()
                projects = Project.objects.all().filter(user=request.user)
                form2 = projectform()
                return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})
        elif 'subtasksubmit' in request.POST:
            form3 = subtaskform(request.POST)
            if form3.is_valid():
                newtask = Task(title=form3.cleaned_data['title'])
                newtask.do_date = form3.cleaned_data['dodate']
                newtask.due_date = form3.cleaned_data['duedate']
                newtask.progress = form3.cleaned_data['progress']
                newtask.description = form3.cleaned_data['description']
                newtask.project = form3.cleaned_data['project']
                newtask.parent = form3.cleaned_data['parent']
                newtask.is_sub = True
                newtask.user = request.user
                newtask.save()
                weekly = Task.objects.filter(
                    due_date__range=[start_week, end_week])
                daily = Task.objects.filter(
                    due_date__date=datetime.date.today())
                tasks = Task.objects.all().filter(user=request.user)
                form3 = subtaskform()
                return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})
    return render(request, 'task/home.html', {'users': users, 'tasks': tasks, 'projects': projects, 'form': form, 'form2': form2, "form3": form3, 'form4': form4, "currentproject": project, "weekly": weekly, "daily": daily})