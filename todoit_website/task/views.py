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
    print("HELLO3")
    print(request)
    #User.objects.all().delete()
    if request.method=='POST':
      print("HELLO4")
      if 'loginbutton' in request.POST:
      	print("in here 1")
      	tryform=loginform(request.POST)
      	if tryform.is_valid():
	        username = tryform.cleaned_data['username']
	        password = tryform.cleaned_data['password']
       		print("in here 2")
       		print(password)
	        user = authenticate(username=username,password=password)
	        print(user)
	        if user is not None:
	        	print("hello")
	        	if user.is_active:
	        		auth_login(request,user)
	        		messages.success(request,username)
	        		template='task/home.html'
	        		return HttpResponseRedirect('home')
                
      elif 'registerbutton' in request.POST:
          print("HELLO1")
          signupform=registerform(request.POST)
          if signupform.is_valid():
              newuser=User(email=signupform.cleaned_data['email'])
              newuser.first_name=signupform.cleaned_data['firstname']
              newuser.last_name=signupform.cleaned_data['lastname']
              newuser.username=signupform.cleaned_data['username']
              newuser.password=signupform.cleaned_data['password']
              newuser.set_password(signupform.cleaned_data['password'])
              print("gets here")
              newuser.last_login = timezone.now() 
              newuser.save()
              print(newuser.username)
              print(newuser.password)
              print("and here")
              messages.success(request,newuser.email)
              template='task/home.html'
              form = taskform()
              form2 = projectform()
              form3 = subtaskform()
              tasks=Task.objects.all()
              projects=Project.objects.all()
              users=User.objects.all()
              return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2,"form3":form3})
          
    cform=registerform()
    lform=loginform()

    return render(request,'task/login.html',{"registerform":cform,"loginform":lform})


# @login_required
def home(request):
    # if this is a POST request we need to process the form data
    # Task.objects.all().delete()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if 'tasksubmit' in request.POST:
            form = taskform(request.POST)
            form2 = projectform()
            form3=subtaskform()
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                newtask=Task(title=form.cleaned_data['title'])
                newtask.do_date=form.cleaned_data['dodate']
                newtask.due_date=form.cleaned_data['duedate']
                newtask.progress=form.cleaned_data['progress']
                newtask.description=form.cleaned_data['description']
                newtask.save()
                tasks=Task.objects.all()
                projects=Project.objects.all()
                users=User.objects.all()
                form=taskform()
                return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2,"form3":form3})
        elif 'projectsubmit' in request.POST:
            form = taskform()
            form2 = projectform(request.POST)
            form3=subtaskform()
            # check whether it's valid:
            if form2.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                newpro=Project(title=form2.cleaned_data['title'])
                newpro.due_date=form2.cleaned_data['duedate']
                newpro.save()
                tasks=Task.objects.all()
                projects=Project.objects.all()
                users=User.objects.all()
                form2=projectform()
                return render(request, 'task/home.html', {'users':users,'tasks':tasks,'projects':projects,'form': form, 'form2':form2,"form3":form3})
        elif 'subtasksubmit' in request.POST:
            form = taskform()
            form2 = projectform()
            form3 = subtaskform(request.POST)
            if form3.is_valid():
                tasks=Task.objects.all()
                projects=Project.objects.all()
                users=User.objects.all()
                form3=subtaskform()
                return render(request, 'task/home.html', {'users':users,'tasks':tasks,'projects':projects,'form': form, 'form2':form2, "form3":form3})
            
            
    form = taskform()
    form2 = projectform()
    form3 = subtaskform()
    tasks=Task.objects.all()
    projects=Project.objects.all()
    users=User.objects.all()
    return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2, "form3":form3})


#pbkdf2_sha256$100000$twFZOefwKMsn$Q19ITpa+fyzEW0R0q/vOyJtAdIwkMrowVSKJK74K/5Q=
#pbkdf2_sha256$100000$urrwW070p6dB$1KQkbZHEVVKMDK82UjDdvZgnzN8LY1y/jmODU9S+FNQ=