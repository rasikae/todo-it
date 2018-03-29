from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import taskform
from .forms import projectform
from .forms import createform
from .forms import loginform
from .forms import subtaskform
from .models import Task
from .models import User
from django.contrib.auth.decorators import login_required
from .models import Project
# Create your views here.

def login(request):
    print("HELLO3")
    if request.method=='POST':
      print("HELLO4")
      if 'login' in request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email,password=password)
        if user is not None:
        	if user.is_active:
        		login(request,user)
        		messages.success(request,email)
        		template='task/home.html'
                
      elif 'create' in request.POST:
          print("HELLO1")
          signupform=createform(request.POST)
          if signupform.is_valid():
              newuser=User(email=signupform.cleaned_data['email'])
              newuser.password=signupform.cleaned_data['password']
              newuser.name=signupform.cleaned_data['name']
              newuser.save()
              messages.success(request,newuser.email)
              template='task/home.html'
              form = taskform()
              form2 = projectform()
              form3 = subtaskform()
              tasks=Task.objects.all()
              projects=Project.objects.all()
              users=User.objects.all()
              return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2,"form3":form3})
          
          
    cform=createform()
    lform=loginform()
    return render(request,'task/login.html',{"signupform":cform,"loginform":lform})

   
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
                return render(request, 'task/home.html', {'users':users,'tasks':tasks,'projects':projects,'form': form, 'form2':form2,"form3":form3})
        elif 'subtasksubmit' in request.POST:
            form = taskform()
            form2 = projectform()
            form3 = subtaskform(request.POST)
            if form3.is_valid():
                tasks=Task.objects.all()
                projects=Project.objects.all()
                users=User.objects.all()
                return render(request, 'task/home.html', {'users':users,'tasks':tasks,'projects':projects,'form': form, 'form2':form2, "form3":form3})
            
            
    form = taskform()
    form2 = projectform()
    form3 = subtaskform()
    tasks=Task.objects.all()
    projects=Project.objects.all()
    users=User.objects.all()
    return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2, "form3":form3})
