class ObjJsonPrinter:
	def render(self, obj, with_values):
		json = {'name':obj.name, 'type':obj.type}

		if with_values:
			if len(obj.values) == 1:
				for val, nbval in obj.values.iteritems():
					if nbval == 1:
						json['values'] = "%s"% str(val)
					else:
						json['values'] = "Always: %s"% str(val)
			elif len(obj.values) > 1:
				json['values'] = obj.values

		if obj.is_optional():
			json['optional'] = "Optional: only %d value(s) over the %d items"% (obj.nb_times_it_exists, obj.nb_times_it_is_expected)
			
		if obj.type == "list":
			if obj.nb_items_min <> None:
				json['list_size'] = "%d to %d"% (obj.nb_items_min, obj.nb_items)
			else:
				json['list_size'] = "%d"% obj.nb_items
				
		if len(obj.childs) > 0:
			if len(obj.childs) == 1 and obj.childs[0].name == "[x]":
				childs_array = obj.childs[0].childs
			else:
				childs_array = obj.childs
			childs_json = []
			for child in childs_array:
				child_json = self.render(child, with_values)
				if child_json <> None:
					childs_json.append(child_json)
			json['childs'] = childs_json
		
		return json
