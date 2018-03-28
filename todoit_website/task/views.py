from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


#from django.template import loader

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




# @login_required
def home(request):
   return render(request,'task/home.html')

def login(request):
   return render(request,'task/login.html')
