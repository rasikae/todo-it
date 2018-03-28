from django.shortcuts import render
#from django.template import loader\\
from django.http import HttpResponseRedirect
from .forms import taskform
from .forms import projectform
from .models import Task
from .models import Project
# Create your views here.

def login(request):
   return render(request,'task/login.html')

def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        if 'tasksubmit' in request.POST:
            form = taskform(request.POST)
            form2 = projectform()
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                newtask=Task(title=form.cleaned_data['title'])
                newtask.do_date=form.cleaned_data['dodate']
                newtask.due_date=form.cleaned_data['duedate']
                newtask.progress=form.cleaned_data['progress']
                newtask.desc=form.cleaned_data['desc']
                newtask.save()
                tasks=Task.objects.all()
                projects=Project.objects.all()
                return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2})
        elif 'projectsubmit' in request.POST:
            form = taskform()
            form2 = projectform(request.POST)
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
                return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2})
            
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = taskform()
        form2 = projectform()
    form = taskform()
    form2 = projectform()
    tasks=Task.objects.all()
    projects=Task.objects.all()
    return render(request, 'task/home.html', {'tasks':tasks,'projects':projects,'form': form, 'form2':form2})