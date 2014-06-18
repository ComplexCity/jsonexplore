class ObjJsonPrinter:
	def render(self, obj, with_values):
		json = {'type':obj.type, 'level':obj.level}
		
		if obj.name == '[x]':
			json['name'] = '?'
		else:
			json['name'] = obj.name
		if obj.type == "dict":
			json['name'] = "{ " + json['name'] + " }"
		elif obj.type == "list":
			json['name'] = "[ " + json['name'] + " ]"

		if with_values:
			values_summary = obj.get_values_summary()
			if len(values_summary) > 0:
				json['values'] = values_summary
			if values_summary is not list:
				sample_value = obj.get_sample_value()
				if sample_value <> None:
					json['sample_value'] = sample_value
			
		if obj.is_optional():
			json['optional'] = "Optional: only %d value(s) over the %d items"% (obj.nb_times_it_exists, obj.nb_times_it_is_expected)
			
		if obj.type == "list":
			if obj.nb_items_min <> None:
				json['list_size'] = "%d to %d"% (obj.nb_items_min, obj.nb_items)
			else:
				json['list_size'] = "%d"% obj.nb_items
				
		if len(obj.children) > 0:
			children_json = []
			for child in obj.children:
				children_json.append(self.render(child, with_values))
			json['children'] = children_json
		
		return json
