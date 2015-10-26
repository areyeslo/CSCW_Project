import io
import pycurl
import json

import stem.process

from stem.util import term

SOCKS_PORT = 7000


def query(url):
	"""
	Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
	"""

	output = io.BytesIO()

	query = pycurl.Curl()
	query.setopt(pycurl.URL, url)
	query.setopt(pycurl.PROXY, 'localhost')
	query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
	query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
	query.setopt(pycurl.WRITEFUNCTION, output.write)

	try:
		query.perform()
		return output.getvalue()
	except pycurl.error as exc:
		return "Unable to reach %s (%s)" % (url, exc)


# Start an instance of Tor configured to only exit through Russia. This prints
# Tor's bootstrap information as it starts. Note that this likely will not
# work if you have another Tor instance running.

def print_bootstrap_lines(line):
	if "Bootstrapped " in line:
		print(term.format(line, term.Color.BLUE))


print(term.format("Starting Tor:\n", term.Attr.BOLD))

tor_process = stem.process.launch_tor_with_config(
	config = {
		'SocksPort': str(SOCKS_PORT),
	},
	init_msg_handler = print_bootstrap_lines,
)

print("\nChecking our endpoint:\n")
email = json.loads(query("https://api.github.com/users/zir").decode("utf-8"))
print(email)
tor_process.kill()  # stops tor