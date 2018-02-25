class Task:
	def __init__(self, iD, title, description, do_date, due_date, progess, tags, parent_project, parent_task, subtasks):
		self.iD = iD
		self.title = title
		self.description = description
		self.do_date = do_date
		self.due_date = due_date
		self.progess = progess
		self.tags = tags
		self.parent_project = parent_project
		self.parent_task = parent_task
		self.subtasks = subtasks


	#Change functions for all the varibles
	def change_title(new):
		self.title = new

	def change_description(new):
		self.description = new

	def change_do_date(new):
		self.do_date = new

	def change_due_date(new):
		self.due_date= new

	def change_progress(new):
		self.progess = new

	def change_tags(new):
		self.tags= new

	def change_parent_project(new):
		self.parent_project = new

	def change_parent_task(new):
		self.parent_task = new

	def change_subtasks(new):
		self.subtasks = new

	#Getter Functions
	#should these be const?
	def get_iD():
		return self.iD

	def get_title():
		return self.title 

	def get_description():
		return self.description 

	def get_do_date():
		return self.do_date 

	def get_due_date():
		return self.due_date

	def get_progress():
		return self.progess 

	def get_tags():
		return self.tags

	def get_parent_project():
		return self.parent_project 
	
	def get_parent_task():
		return self.parent_task

	def get_subtasks():
		return self.subtasks 