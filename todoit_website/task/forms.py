from django import forms

class taskform(forms.Form):
		# iD = forms.UUIDField(label='ID', max_length=100)
    title = forms.CharField(label='Title', max_length=128)
    dodate = forms.DateTimeField(label='Do-Date')
    duedate = forms.DateTimeField(label='Due-Date')
    progress = forms.CharField(label='Progress', max_length=20)
    description = forms.CharField(label='Description', max_length=100)
    project = forms.CharField(label='Project', max_length=128)
    
class subtaskform(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    dodate = forms.DateTimeField(label='Do-Date')
    duedate = forms.DateTimeField(label='Due-Date')
    progress = forms.CharField(label='Progress', max_length=20)
    description = forms.CharField(label='Description', max_length=100)
    parent = forms.CharField(label='Parent', max_length=128)
    project = forms.CharField(label='Project', max_length=128)
    
class projectform(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    duedate = forms.DateTimeField(label='Due-Date')
    parent = forms.CharField(label='Parent', max_length=128)

class createform(forms.Form):
    name=forms.CharField(label='Name', max_length=128)
    email=forms.EmailField(label='Email', max_length=128)
    password=forms.CharField(label='Password', max_length=128)
    
class loginform(forms.Form):
    email=forms.EmailField(label='Email', max_length=128)
    password=forms.CharField(label='Password', max_length=128)

