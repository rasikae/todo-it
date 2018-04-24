class Project:
	def __init__(self, iD, title, description, due_date, progress, tags, parent_project, tasks):
		self.iD = iD
		self.title = title
		self.description = description
		self.due_date = due_date
		self.progress = progress
		self.tags = tags
		self.parent_project = parent_project
		self.tasks = tasks

	#Change functions for all the varibles
	def change_title(new):
		self.title = new

	def change_description(new):
		self.description = new

	def change_due_date(new):
		self.due_date= new

	def change_progress(new):
		self.progress = new

	def change_tags(new):
		self.tags= new

	def change_parent_project(new):
		self.parent_project = new

	def change_tasks(new):
		self.tasks = new

	#Getter Functions
	#should these be const?
	def get_iD():
		return self.iD

	def get_title():
		return self.title 

	def get_description():
		return self.description 

	def get_due_date():
		return self.due_date

	def get_progress():
		return self.progress 

	def get_tags():
		return self.tags

	def get_parent_project():
		return self.parent_project 

	def get_tasks():
		return self.tasks 