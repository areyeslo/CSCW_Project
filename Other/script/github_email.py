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

import sys
import requests
import argparse
import json
import deep_search

def get_github_email(username):
    """Search for a users email address associated with their GitHub account.

    Args:
            username (str): The username to search against.

    Returns:
            str: The email address associated with the GitHub account.
    """
    ACCESS_TOKEN = "YOUR TOKEN HERE"
    request_list = [
        'https://api.github.com/users/' + username +
        '?access_token=' + ACCESS_TOKEN,
        'https://api.github.com/users/' + username +
		'/events/public?access_token=' + ACCESS_TOKEN]

    for url in request_list:
        request = requests.get(url)
        data = json.loads(request.text)
        result = deep_search.search(data, "email")
        if result != ("" or None):
            return result


#    ##     ##    ###    ######## ##     ##
#    ###   ###   ## ##      ##    ###    ##
#    #### ####  ##   ##     ##    ####   ##
#    ## ### ## #########    ##    ## ### ##
#    ##  #  ## ##     ##    ##    ##   ####
#    ##     ## ##     ##    ##    ##    ###
#    ##     ## ##     ## ######## ##     ##
##########################################################################

def main(args=None):
    parser = argparse.ArgumentParser(description="""Search for a users email
		address associated with their GitHub account.""")

    parser.add_argument("username", nargs=1, help="""The username to search
		against.""")

    args = parser.parse_args()

    print (get_github_email(args.username[0]))

if __name__ == "__main__":
    main()
