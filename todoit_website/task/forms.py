from django import forms

class taskform(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    dodate = forms.DateTimeField(label='Do-Date')
    duedate = forms.DateTimeField(label='Due-Date')
    progress = forms.CharField(label='Progress', max_length=20)
    desc = forms.CharField(label='Description', max_length=100)
    
class projectform(forms.Form):
    title = forms.CharField(label='Title', max_length=128)
    duedate = forms.DateTimeField(label='Due-Date')
   