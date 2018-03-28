from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import taskform
from .models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_user(request):

	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user is not None:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect("home")

def login(request):
   return render(request,'task/login.html')
   
def hometask(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
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
            return render(request, 'task/hometask.html', {'tasks':results,'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = taskform()
        
    return render(request,'task/hometask.html',{'form':form})
   
# @login_required
def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = taskform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            newtask=Task(iD='1')
            newtask.title=form.cleaned_data['title']
            newtask.do_date=form.cleaned_data['dodate']
            newtask.due_date=form.cleaned_data['duedate']
            newtask.progress=form.cleaned_data['progress']
            newtask.desc=form.cleaned_data['desc']
            newtask.save()
            results=Task.objects.all()
            return render(request, 'task/hometask.html', {'tasks':results,'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = taskform()

    return render(request, 'task/home.html', {'form': form})