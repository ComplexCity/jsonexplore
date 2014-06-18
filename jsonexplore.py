from ObjBuilder import ObjBuilder
from ObjTextPrinter import ObjTextPrinter
from ObjJsonPrinter import ObjJsonPrinter
from ObjJsPrinter import ObjJsPrinter
from sys import argv
import json

use_string = """Use: python jsonexplore.py input_json_file [no_value]
	input_json_file: path to the json file to explore
	no_value: optional parameter saying you don't want to explore the values\n
	examples:
		python jsonexplore.py my_file.json
		python jsonexplore.py my_file.json no_value"""

output_json_file = "obj.json"
output_js_file = "obj.js"

class InitError(Exception):
	pass

try:
	input_json_file = argv[1]
	with_values = True
	if len(argv) > 2:
		if argv[2] == 'no_value':
			with_values = False
		else:
			raise InitError("If used, the second parameter should be 'no_value'")
	f = open(input_json_file, 'r')
	loaded_json = json.load(f)
	f.close()

	builder = ObjBuilder(loaded_json)
	obj = builder.get_obj()
	
	text_printer = ObjTextPrinter()
	print text_printer.render(obj, with_values)

	json_printer = ObjJsonPrinter()
	obj_json = json_printer.render(obj, with_values)
	f = open(output_json_file, 'w')
	json.dump(obj_json, f)
	f.close()
	#print json.dumps(obj_json)
	
	js_printer = ObjJsPrinter(input_json_file)
	obj_js = js_printer.render(obj, with_values)
	f = open(output_js_file, 'w')
	f.write(obj_js)
	f.close()
	
except IndexError:
	print "The parameter input_json_file is missing"
	print "\n%s"% use_string
except IOError:
	print "No such file or directory: '%s'"% argv[1]
	print "\n%s"% use_string
except InitError as e:
	print e
	print "\n%s"% use_string
except ValueError as e:
	print "The JSON file cannot be loaded"
	print e
	print "\n%s"% use_string

	



