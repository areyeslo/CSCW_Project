import requests
import json

"""
Gets a GitHub account email address
"""
def extractaddress(user, proxies=None, oauth_token=None):
	try_token = ""
	if(oauth_token==None): oauth_token = [""]
	else: try_token = "?access_token=" + oauth_token[0]
	result = requests.get('https://api.github.com/users/' + user + '/events/public' + try_token, proxies=proxies)
	data = json.loads(result.text)
	for item in data:
		try: return item["payload"]["commits"][0]["author"]["email"]
		except: pass

print(extractaddress("breckwagner", oauth_token=["e306acd6925b12530f9f811556e29025d246f6f0"]))