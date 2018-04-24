import task
import project
import uuid
class User:
	def __init__(self, iD, name, email, tasks, projects):
		self.iD = iD
		self.name = name
		self.email = email
		self.tasks = tasks  #list of Task Objects
		self.projects = projects #list of Project Objects
	
	#Change functions for all the varibles

	def change_name(new):
		self.name = new

	def change_email(new):
		self.email = new

	def add_task():
		#create task object 
		#get information from the user
		task1 = Task(uuid.uuid4(), title, description, do_date, due_date, progess, tags, parent_project, subtasks)
		#add new task to the list
		tasks.append(task1)

	def add_project():
		#create project object 
		#get information from the user
		project1 = Project(uuid.uuid4(), title, description, due_date, progess, tags, parent_project, task)
		#add new project to the list
		projects.append(project1)

	#Getter Functions
	def get_name(new):
		return self.name

	def get_email(new):
		return self.email

	def get_task(new):
		return tasks

	def get_project(new):
		return projects