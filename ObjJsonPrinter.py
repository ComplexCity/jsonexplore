class ObjJsonPrinter:
	def render(self, obj, with_values):
		json = {'name':obj.name, 'type':obj.type}

		if with_values:
			values_summary = obj.get_values_summary()
			if len(values_summary) > 0:
				json['values'] = values_summary
			
		if obj.is_optional():
			json['optional'] = "Optional: only %d value(s) over the %d items"% (obj.nb_times_it_exists, obj.nb_times_it_is_expected)
			
		if obj.type == "list":
			if obj.nb_items_min <> None:
				json['list_size'] = "%d to %d"% (obj.nb_items_min, obj.nb_items)
			else:
				json['list_size'] = "%d"% obj.nb_items
				
		if len(obj.children) > 0:
			if len(obj.children) == 1 and obj.children[0].name == "[x]":
				if len(obj.children[0].children) > 0:
					children_array = obj.children[0].children
				else:
					children_array = obj.children
			else:
				children_array = obj.children
			children_json = []
			for child in children_array:
				child_json = self.render(child, with_values)
				if child_json <> None:
					children_json.append(child_json)
			json['children'] = children_json
		
		return json
