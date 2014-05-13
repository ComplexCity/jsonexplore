class Obj:
	def __init__(self, path):
		self.path = path
		parts = path.split("/")
		self.level = len(parts) - 2	
		self.name = parts[self.level]
		
		self.type = None
		self.values = {}
		self.nb_times_it_exits = 0
		self.nb_times_it_is_expected = 1
		self.nb_items = 1
		self.childs = []
		
	def add_child(self, child):
		self.childs.append(child)
	
	def is_optional(self):
		if self.nb_times_it_exists <> self.nb_times_it_is_expected:
			return True
		return False
						
						