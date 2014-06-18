from ObjJsonPrinter import ObjJsonPrinter
import json

class ObjJsPrinter:
	_widths = [[]]
	
	def __init__(self, filename):
		self.filename = filename
		
	
	def _setWidths(self, obj, level):
		if obj.type == "dict":
			self._widths[level].append(len("{ %s }"% obj.name))
		elif obj.type == "list":
			if obj.nb_items_min <> None:
				self._widths[level].append(len("[ %s ] (%d to %d)"% (obj.name, obj.nb_items_min, obj.nb_items)))
			else:
				self._widths[level].append(len("[ %s ] (%d)"% (obj.name, obj.nb_items)))
		else:
			self._widths[level].append(len(obj.name))
		if len(obj.children) > 0:
			if len(self._widths) < level + 2:
				self._widths.append([])
			for child in obj.children:
				self._setWidths(child, level + 1)
	
	def render(self, obj, with_values):
		self._setWidths(obj, 0)
		widths = []
		for widths_array in self._widths:
			widths.append(max(widths_array))
			
		data = {'filename': self.filename,
			'widths': widths,
			'json': ObjJsonPrinter().render(obj, with_values)}
		return "var obj = " + json.dumps(data) + ";"
