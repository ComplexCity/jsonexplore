from ObjBuilder import ObjBuilder
from ObjTextPrinter import ObjTextPrinter
from ObjJsonPrinter import ObjJsonPrinter
import json

json_file = "test.json"
obj_json_file = "res.json"

builder = ObjBuilder(json_file)
obj = builder.get_obj()

#print "---------------------------------"
text_printer = ObjTextPrinter()
#print text_printer.render(obj, False)


print "---------------------------------"
json_printer = ObjJsonPrinter()
obj_json = json_printer.render(obj, True)
f = open(obj_json_file, 'w')
json.dump(obj_json, f)
f.close()
#print json.dumps(obj_json)

