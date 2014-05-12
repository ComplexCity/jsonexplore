class Obj:
	def __init__(self, path):
		self.path = path
		parts = path.split("/")
		self.level = len(parts) - 2	
		self.name = parts[self.level]
		self.childs = []
		self.type = None
		self.values = {}
		
	def add_child(self, child):
		self.childs.append(child)