from django.shortcuts import render
#from django.template import loader

# Create your views here.
def home(request):
   return render(request,'task/home.html')
