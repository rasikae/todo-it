from django import forms

class taskform(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    dodate = forms.DateTimeField(label='Do-Date')
    duedate = forms.DateTimeField(label='Due-Date')
    progress = forms.CharField(label='Progress', max_length=20)
    description = forms.CharField(label='Description', max_length=100)
    # project = forms.CharField(label='Project', max_length=128)
    
class subtaskform(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    dodate = forms.DateTimeField(label='Do-Date')
    duedate = forms.DateTimeField(label='Due-Date')
    progress = forms.CharField(label='Progress', max_length=20)
    description = forms.CharField(label='Description', max_length=100)
    # parent = forms.CharField(label='Parent', max_length=128)
    # project = forms.CharField(label='Project', max_length=128)
    
class projectform(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    duedate = forms.DateTimeField(label='Due-Date')
    # parent = forms.CharField(label='Parent', max_length=128)

class registerform(forms.Form):
    firstname=forms.CharField(label='',max_length=128,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    lastname=forms.CharField(label='',max_length=128,widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email=forms.EmailField(label='',max_length=128,widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(label='',max_length=128,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(label='',max_length=128,widget=forms.TextInput(attrs={'placeholder':'Password'}))
    
class loginform(forms.Form):
    # email=forms.EmailField(max_length=128,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    username=forms.CharField(label='',max_length=128,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password=forms.CharField(label='',max_length=128,widget=forms.TextInput(attrs={'placeholder':'Password','type':'password'}))

