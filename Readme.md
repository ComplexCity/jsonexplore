##What these scripts do
The purpose of the scripts in this repository is to explore an input JSON file to give insight into its content: its architecture, its fields and their different values.

The main script is _jsonexplore.py_. It explores the given JSON file and build a tree of _Obj_ objects from it thanks to the _ObjBuilder_. Then it renders the tree of _Obj_ using a printer. Tree basic printers are avalaible at this time:

-	The _ObjTextPrinter_ will simply output a string describing the tree, printed on console
-	The _ObjJsonPrinter_ will output a JSON dictionary, written in the output _obj.json_ file
-	The output JSON file can be used as the input of the _ObjHtmlPrinter_ to display a D3.js tree.

##The _Obj_ class
An _Obj_ is created for each key of the given JSON dictionary.

###Properties
-	**name**: the name of the field or "." for root

-	**path**: the path of the field from root

-	**level**: the distance from root

-	**type**: the type of its value(s) (e.g. dict, list, unicode, int…)

-	**values**: a dictionary associating to each existing value the number of times this value is found (see also the methods).

-	**nb_times_it_exists**: if this field is part of an item in a list, it says how many items in the list have this field

-	**nb_times_it_is_expected**: if this field is part of an item in a list, it says how many items are in the list, that is to say how many times this field should appear

-	**nb_items**: in case of a list, it says how many items it contains (basically it is the length of the list). If this list exists as an item of a parent list, it says the max length of the list.

-	**nb_items_min**: in case of a list existing as an item of a parent list, it says the min length of the list

-	**children**: in case of a dictionary, it is the list of its keys each one reprensented by an _Obj_ instance

###Methods
-	**is_optional()**: if the field is part of an item in a list, it says if this field is sometimes missing in the other items of the list, in other words if _nb_times_it exists_ is different from _nb_times_it_is_expected_. If it is optional, it returns _True_. Otherwise, it return _False_.

-	**(string) get_values_summary()**: depending on the **values** property, it returns a string or a list offering a more comprehensible version of the **values** dictionary :
	-	"'_value_'"	if there is only one value, used only once
	-	"Always '_value_'" if there is only one value, used more than once
	- 	"Always empty" if the value is always an empty string
	- 	"All different values" if each item has a different value
	-	"Almost all different values (each value appear from _x_ to _y_ times)" if every value is used less than 5 times
	- 	a list where each value is reprensented by a dictionary with 2 keys:

			{
				'value': the_value,
				'count': the_number_of_times_this_value_is_used
			}
			
	This method is used by the _ObjJsonPrinter_, and consequently by the _ObjHtmlPrinter_ to display the values.
	

-	**get_sample_value()**: it returns the first value that is not an empty string or _None_ if not found.

##The _ObjTextPrinter_
Example of output:

	|- .: a Dict composed of:
		|- statuses: a List composed of 10 items like:
			|- [x]: a Dict composed of:
				|- attitudes_count: int - values:
					'0' [7]
					'1' [3]
				|- bmiddle_pic (Optional: only 6 value(s) over the 10 items): unicode - values:
					'http://ww3.sinaimg.cn/bmiddle/4bed07b4jw1ef4pyzb9kzj20uh15ok33.jpg' [1]
					'http://ww4.sinaimg.cn/bmiddle/664b3fe9jw1ef4px8ca0uj20bv0ft40f.jpg' [1]
					'http://ww4.sinaimg.cn/bmiddle/9f767fc7jw1ef4prguk4tj20hs0npdjc.jpg' [1]
					'http://ww3.sinaimg.cn/bmiddle/4d3ffe9ejw1ef4q0uogdtj20xc18gguu.jpg' [1]
					'http://ww1.sinaimg.cn/bmiddle/df92068ejw1ef4pqnefs2j20xc18gjyx.jpg' [1]
					'http://ww4.sinaimg.cn/bmiddle/8bf1e5b4jw1ef4pxgzavsj20f00qo756.jpg' [1]
				|- comments_count: int - values:
					'0' [9]
					'1' [1]
				|- distance: int - values:
					'400' [1]
					'1700' [1]
					'1800' [3]
					'1900' [1]
					'2000' [2]
					'1400' [1]
					'1500' [1]
				|- favorited: bool (always: 'False')
				|- in_reply_to_user_id: unicode (always: '')
				|- mid: unicode - values:
					'3696007882016559' [1]
					'3696009920372953' [1]
					'3696010247357290' [1]
					'3696007861039896' [1]
					'3696010012795278' [1]
					'3696009530197458' [1]
					'3696008955203962' [1]
					'3696009429891580' [1]
					'3696008082926243' [1]
					'3696010490692288' [1]
				|- reposts_count: int (always: '0')
				|- truncated: bool (always: 'False')
				|- user: a Dict composed of:
					|- allow_all_comment: bool - values:
						'False' [3]
						'True' [7]
					|- location: unicode - values:
						'上海 普陀区' [5]
						'湖北 襄阳' [1]
						'其他' [1]
						'上海 黄浦区' [1]
						'上海 闸北区' [1]
		|- total_number: int (value: '129751')
	
##The _ObjJsonPrinter_
Example of output:

	{	"type":"dict",
		"name":".",
		"children":[
			{
				"children":[
					{
						"sample_value":"'0'",
						"values":[
							{
								"count":7,
								"value":0
							},
							{
								"count":3,
								"value":1
							}
						],
						"type":"int",
						"name":"attitudes_count"
					},
					{
						"sample_value":"'http://ww3.sinaimg.cn/bmiddle/4bed07b4jw1ef4pyzb9kzj20uh15ok33.jpg'",
						"values":"All different values",
						"type":"unicode",
						"name":"bmiddle_pic",
						"optional":"Optional: only 6 value(s) over the 10 items"
					},
					{
						"sample_value":"'0'",
						"values":[
							{
								"count":9,
								"value":0
							},{
								"count":1,
								"value":1
							}
						],
						"type":"int",
						"name":"comments_count"
					},
					{
						"sample_value":"'400'",
						"values":"Almost all different values (each value appears from 1 to 3 times)",
						"type":"int",
						"name":"distance"
					},
					{
						"values":"Always 'False'",
						"type":"bool",
						"name":"favorited"
					},
					{
						"values":"Always ''",
						"type":"unicode",
						"name":"in_reply_to_user_id"
					},
					{
						"sample_value":"'3696007882016559'",
						"values":"All different values",
						"type":"unicode",
						"name":"mid"
					},
					{
						"values":"Always '0'",
						"type":"int",
						"name":"reposts_count"
					},
					{
						"values":"Always 'False'",
						"type":"bool",
						"name":"truncated"
					},
					{
						"type":"dict",
						"name":"user",
						"children":[
							{
								"sample_value":"'False'",
								"values":[
									{
										"count":3,
										"value":false
									},
									{	"count":7,
										"value":true
									}
								],
								"type":"bool",
								"name":"allow_all_comment"
							},
							{
								"sample_value":"'上海 普陀区'",
								"values":"Almost all different values (each value appears from 1 to 5 times)",
								"type":"unicode",
								"name":"location"
							}
						]
					}
				],
				"type":"list",
				"name":"statuses",
				"list_size":"10"
			},
			{
				"values":"'129751'",
				"type":"int",
				"name":"total_number"
			}
		]
	}
	
##The _ObjHtmlPrinter_
You can see a working example [here](http://catwomanlair.net/complexcity/).

This visualisation is based on [D3js](http://d3js.org) and inspired by others great work and howtos:

-	[Federal Budget Data Vizualization D3.js](http://www.brightpointinc.com/interactive/budget/index.html?source=d3js)
-	[D3.js Tips and Tricks: Tree diagrams in d3.js](http://www.d3noob.org/2014/01/tree-diagrams-in-d3js_11.html)
-	[Mike Bostock - Tree Layout](https://github.com/mbostock/d3/wiki/Tree-Layout)
-	[Mike Bostock - Let's Make a Bar Chart](http://bost.ocks.org/mike/bar/)