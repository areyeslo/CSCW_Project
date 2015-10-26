

#import json
#import urllib.request
#local_filename, headers = urllib.request.urlretrieve('http://api.stackexchange.com/2.2/users/123?order=desc&sort=reputation&site=stackoverflow')
#f = open(local_filename)
#data = json.load(f)
#print(f.read())

"""
import urllib.parse
import urllib.request

url = 'http://api.stackexchange.com/2.2/users/123'
values = {
	'order' : 'desc',
	'sort' : 'reputation',
	'site' : 'stackoverflow'
}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
	the_page = response.read()
	print(the_page)
"""


"""
import xml.etree.cElementTree
e = xml.etree.cElementTree.parse('Users.xml').getroot()

for event, elem in xml.etree.cElementTree.iterparse(xmL, events=('start', 'end', 'start-ns', 'end-ns')):
	print(event, elem)
"""

import xml.etree.ElementTree as etree
xmL = 'Users.xml'
for event, elem in etree.iterparse(xmL, events=('start', 'end', 'start-ns', 'end-ns')):
	print (event, elem)