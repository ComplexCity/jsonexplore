from Obj import Obj
import json

class ObjBuilder:
	my_types = {}
	my_values = {}
	
	def __init__(self, json_file):
		f = open(json_file, 'r')
		self.loaded_json = json.load(f)
		f.close()

	def load_simple(self, path, s):
		self.my_types[path] = type(s).__name__
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
					raise "Different kinds od items in list %s"% path
		return res
		
	def load_list(self, path, l):
		self.my_types[path] = "list"
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
#		for key in sorted_keys:
#			print key
#			print "%s (%s)"% (key, my_types[key])
#		print "======================================"
#		print my_values

		my_parent = {}
		my_obj = {}
		for key in sorted_keys:
			my_parent[key] = 0
			obj = Obj(key)
			obj.type = self.my_types[key]
			if key in self.my_values:
				obj.values = self.my_values[key]
			my_obj[key] = obj
			
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
		

