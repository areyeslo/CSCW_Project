# cssselect

from lxml import html
from lxml.cssselect import CSSSelector
import requests, csv, subprocess, sys, json, atexit


#
#
#
#
#
#
################################################################################

class BreakIt(Exception): pass

counter = 0
max_counter = 600
user_list = []
csv_column = 0
input_file = 'Medium Reputation QueryResults.csv'
output_list = [["stackoverflow_id", "email", "name"]]
seed = '1'
github_oath_token = ["e306acd6925b12530f9f811556e29025d246f6f0"]

def finish():
	with open('output.csv', 'w', newline='') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(output_list)

atexit.register(finish)

"""
Gets a GitHub account email address
This is quick and dirty
"""
def extractaddress(user, proxies=None, oauth_token=None):
	try_token = ""
	if(oauth_token==None): 
		oauth_token = [""]
	else: 
		try_token = "?access_token=" + oauth_token[0]
	result = requests.get('https://api.github.com/users/' + user + '/events/public' + try_token, proxies=proxies)
	data = json.loads(result.text)
	for item in data:
		try: 
			return item["payload"]["commits"][0]["author"]["email"]
		except: 
			pass


with open(input_file, newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
		user_list.append([row[csv_column]])

user_list = user_list[user_list.index([seed]):]


try:
	for user_id in range(1,len(user_list)) :
		page = requests.get('http://stackoverflow.com/users/' + user_list[user_id][0] + '/')
		tree = html.fromstring(page.text)

		subtree = tree.cssselect('.user-links')

		#link_list = ['.icon-github + a', '.icon-twitter + a', '.icon-site + a']
		link_list = ['.icon-github + a']
		
		
		for i in range(len(link_list)) :
			if counter >= max_counter:
				print("Quota Reached")
				raise BreakIt
			result = tree.cssselect(link_list[i])
			if(len(result)==1):
				
				
				bashCommand = "./findGitHubEmail " + result[0].text
				process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
				output = process.communicate()[0]
				output = output.decode("utf-8").rstrip("\n\r")
				
				#output = extractaddress(result[0].text, oauth_token=github_oath_token)
				
				
				if(output!=""):
					user_list[user_id].append(output)
					output_list.append(user_list[user_id])
					print("\n"+str(user_list[user_id]), counter)
					counter += 1
			else:
				user_list[user_id].append("")
				print(str(user_id)+'.',end="",flush=True)


except:
	print ("Unexpected error:", sys.exc_info())
finally:
	with open('output.csv', 'w', newline='') as fp:
		a = csv.writer(fp, delimiter=',')
		a.writerows(output_list)



	
