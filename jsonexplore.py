from ObjBuilder import ObjBuilder
from ObjTextPrinter import ObjTextPrinter

json_file = "test.json"

builder = ObjBuilder(json_file)
obj = builder.get_obj()
text_printer = ObjTextPrinter()
print text_printer.render(obj, True)
#text_printer.render(obj, True)