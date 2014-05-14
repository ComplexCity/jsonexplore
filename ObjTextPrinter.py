class ObjTextPrinter:
	def render(self, obj, with_values):
		shift = ""
		for i in range(0, obj.level):
			shift += "\t"
		s = shift
		s += "|- %s"% obj.name
		if obj.is_optional():
			s+= " (Optional: only %d value(s) over the %d items)"% (obj.nb_times_it_exists, obj.nb_times_it_is_expected)
		s += ": "
		if obj.type == "dict" or obj.type == "list":
			if obj.type == "dict":
				s += "a Dict composed of:"
			elif obj.type == "list":
				s += "a List composed of "
				if obj.nb_items_min <> None:
					s += "%d to %d"% (obj.nb_items_min, obj.nb_items)
				else:
					s += "%d"% obj.nb_items
				s += " items like:"
			for child in obj.childs:
				s += "\n"
				s += self.render(child, with_values)
		else:
			s += obj.type
			if with_values:
				if len(obj.values) == 1:
					for val, nbval in obj.values.iteritems():
						if nbval == 1:
							s += " (value: %s)"% str(val)
						else:
							s += " (always: %s)"% str(val)
				elif len(obj.values) > 1:
					s += " - values:\n"
					if obj.type == "unicode":
						for val, nbval in obj.values.iteritems():
							s += "%s\t%s [%d]\n"% (shift, val, nbval)
					else:
						for val, nbval in obj.values.iteritems():
							s += "%s\t%s [%d]\n"% (shift, str(val), nbval)
					s = s[:-1]
		return s