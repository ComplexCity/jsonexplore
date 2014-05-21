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
		self.nb_items = 0
		self.nb_items_min = None
		self.children = []
		
	def add_child(self, child):
		self.children.append(child)
	
	def is_optional(self):
		if self.nb_times_it_exists <> self.nb_times_it_is_expected:
			return True
		return False
		
	def get_values_summary(self):
		if self.type == 'list' or self.type == 'dict':
			return ""
		if len(self.values) == 1:
			for val, nbval in self.values.iteritems():
				if nbval == 1:
					return "'%s'"% str(val)
				return "Always '%s'"% str(val)
		elif len(self.values) > 1:
			counts = {}
			for count in self.values.values():
				if count in counts:
					counts[count] += 1
				else:
					counts[count] = 1
			max_count = max(counts.keys())
			if max_count <= 5:
				sample = ""
				values = self.values.keys()
				for i in range(0, len(values)):
					sample = values[i] if self.type == 'unicode' else str(values[i])
					if len(sample) > 0:
						break
				if len(counts) == 1 and counts.keys()[0] == 1:
					return "All different values (e.g. '%s')"% sample
				else:
					min_count = min(counts.keys())
					if min_count == max_count:
						return "Almost all different values, each value appears %d times (e.g. '%s')"% (min_count, sample)
					return "Almost all different values, each value appears from %d to %d times (e.g. '%s')"% (min_count, max_count, sample)
			values = []
			for value, count in self.values.iteritems():
				values.append({'value':value, 'count':count})
			return values
		else:
			return "Always empty"
									
						