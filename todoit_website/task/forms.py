from django import forms

# Different choices for progress drop-down
PROGRESS_CHOICES = (
    ('Not Started', 'Not Started'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done'),
)

# Forms used in home and login html files
class taskform(forms.Form):
    title = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Task Title'}))
    dodate = forms.DateTimeField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Do-Date'}))
    duedate = forms.DateTimeField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Due-Date'}))
    progress = forms.ChoiceField(label='Progress', choices=PROGRESS_CHOICES)  #
    description = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Description'}))
    project = forms.CharField(label='', max_length=128, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Parent Project'}))

# The form used to take input for subtasks
class subtaskform(forms.Form):
    title = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Title'}))
    dodate = forms.DateTimeField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Do-Date'}))
    duedate = forms.DateTimeField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Due-Date'}))
    progress = forms.ChoiceField(label='Progress', choices=PROGRESS_CHOICES)
    description = forms.CharField(label='', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Description'}))
    parent = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Parent Task'}))
    project = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Parent Project'}))

# The form used to take input for projects
class projectform(forms.Form):
    title = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Project Title'}))
    duedate = forms.DateTimeField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Due-Date'}))
    parent = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Parent Project'}))

# The form used to take input for registering
class registerform(forms.Form):
    firstname = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    username = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Password'}))

# The form used to take input for logging in
class loginform(forms.Form):
    username = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Password', 'type': 'password'}))

# The form used to take input for collaborating
class collabform(forms.Form):
    name = forms.CharField(label='', max_length=128, widget=forms.TextInput(
        attrs={'placeholder': 'Collaborator Username'}))
