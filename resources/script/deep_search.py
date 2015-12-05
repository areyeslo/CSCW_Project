#!/usr/bin/python3

# The MIT License (MIT)
# 
# Copyright (c) 2015 Richard B. Wagner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

def _iterate(collection, key):
	for item in collection:
		result = search(item, key)
		if result != None:
			return result
	
def _find(collection, key):
	if key in collection: 
		return collection[key]
	else: 
		for item in collection:
			result = search(collection[item], key)
			if result != None:
				return result

def search(obj, key):
	"""Search for key in JSON-like datastructure (nested tuple/dict/list)

	Args:
		obj (collection): The first parameter.
		key (object): The second parameter. Defaults to None.

	Returns:
		object: The first occurance of an object with a key matching the key param. 
			NOTE: dictionaries do not nessisarely have an order.
	"""
	types_of_collections = {
		dict: lambda obj, key: _find (obj, key),
		tuple: lambda obj, key: _iterate(obj, key),
		list: lambda obj, key: _iterate(obj, key)
	}
	for type_of_collection in types_of_collections.keys():
		if isinstance(obj, type_of_collection):
			return types_of_collections[type_of_collection](obj, key)