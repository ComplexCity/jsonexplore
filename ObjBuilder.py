from Obj import Obj
import json

class ObjBuilder:
	my_types = {}
	my_values = {}
	my_nb_items = {}
	my_nb_items_min = {}
	my_paths = {}
	
	def __init__(self, loaded_json):
		self.loaded_json = loaded_json
		
	def count_path(self, path):
		if path in self.my_paths:
			self.my_paths[path] += 1
		else:
			self.my_paths[path] = 1

	def load_simple(self, path, s):
		self.my_types[path] = type(s).__name__
		self.count_path(path)
		if path not in self.my_values:
			self.my_values[path] = {s:1}
		else:
			if s in self.my_values[path].keys():
				self.my_values[path][s] += 1
			else:
				self.my_values[path][s] = 1 
		
	def get_list_type(self, l, path):
		res = None
		if len(l) > 0:
			if isinstance(l[0], dict):
				res = "dict"
			elif isinstance(l[0], list):
				res = "list"
			else:
				res = type(l[0]).__name__
			for item in l:
				if type(item).__name__ <> res:
					raise "Different kinds of items in list %s"% path
		return res
		
	def load_list(self, path, l):
		self.my_types[path] = "list"
		self.count_path(path)
		new_len = len(l)
		if path in self.my_nb_items:
			if new_len <> self.my_nb_items[path]:
				nb = [new_len, self.my_nb_items[path]]
				if path in self.my_nb_items_min:
					nb.append(self.my_nb_items_min[path])
				self.my_nb_items_min[path] = min(nb)
				self.my_nb_items[path] = max(nb)
		else:
			self.my_nb_items[path] = len(l)
		child_path = path + "[x]/"
		res = self.get_list_type(l, path)
		if res <> None:
			for item in l:
				if res == "dict":
					self.load_dict(child_path, item)
				elif res == "list":
					self.load_list(child_path, item)
				else:
					self.load_simple(child_path, item)
		
	def load_dict(self, path, d):
		self.my_types[path] = "dict"
		self.count_path(path)
		for key, value in d.iteritems():
			child_path = path + key + "/"
			if isinstance(value, dict):
				self.load_dict(child_path, value)
			elif isinstance(value, list):
				self.load_list(child_path, value)
			else:
				self.load_simple(child_path, value)
				
	def get_obj(self):
		path = "./"
		self.load_dict(path, self.loaded_json)
		sorted_keys = sorted(self.my_types.keys())
		my_parent = {}
		my_obj = {}
		for key in sorted_keys:
			my_parent[key] = 0
			obj = Obj(key)
			obj.type = self.my_types[key]
			
			if obj.type == "list":
				obj.nb_items = self.my_nb_items[key]
				if key in self.my_nb_items_min:
					obj.nb_items_min = self.my_nb_items_min[key]

			obj.nb_times_it_exists = self.my_paths[key]
				
			if key in self.my_values:
				obj.values = self.my_values[key]
			my_obj[key] = obj
		
		for key in sorted_keys:
			parts = key.split("[x]/")
			parts_len = len(parts)
			if parts_len > 1:
				path = parts[0]
				nb_items = my_obj[path].nb_items
				for i in range(1, parts_len-1):
					path += "[x]/%s"% parts[i]
					nb_items *= my_obj[path].nb_items
				my_obj[key].nb_times_it_is_expected = nb_items
			
		for i in range(0, len(sorted_keys)):
			needle = sorted_keys[i]
			for key in my_parent:
				if len(key) > len(needle) and key.startswith(needle):
					my_parent[key] = i
		for i in range(1, len(sorted_keys)):
			child_index = sorted_keys[i]
			child = my_obj[child_index]
			parent_index = sorted_keys[my_parent[child_index]]
			parent = my_obj[parent_index]
			parent.add_child(child)
			
		return my_obj['./']
		

