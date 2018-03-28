from django.shortcuts import render
#from django.template import loader\\
from django.http import HttpResponseRedirect
from .forms import taskform
from .models import Task
# Create your views here.

def login(request):
   return render(request,'task/login.html')

def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #if projectsubmit
        form = taskform(request.POST)
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
            results=Task.objects.all()
            return render(request, 'task/home.html', {'tasks':results,'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = taskform()
    results=Task.objects.all()
    return render(request, 'task/home.html', {'tasks':results, 'form': form})