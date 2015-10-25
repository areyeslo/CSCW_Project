# cssselect

from lxml import html
from lxml.cssselect import CSSSelector
import requests
import csv
import subprocess


#
#
#
#
#
#
################################################################################

user_list = []
csv_column = 0

with open('Medium Reputation QueryResults.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
		user_list.append([row[csv_column]])


for user_id in range(1,len(user_list)) :
	page = requests.get('http://stackoverflow.com/users/' + user_list[user_id][0] + '/')
	tree = html.fromstring(page.text)

	subtree = tree.cssselect('.user-links')

	#link_list = ['.icon-github + a', '.icon-twitter + a', '.icon-site + a']
	link_list = ['.icon-github + a']
	for i in range(len(link_list)) :
		result = tree.cssselect(link_list[i])
		if(len(result)==1):
			print(result[0].text)
			bashCommand = "./findGitHubEmail " + result[0].text
			process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
			output = process.communicate()[0]
			
			# add email address to list
			user_list[user_id].append(output)
			print(user_list[user_id])