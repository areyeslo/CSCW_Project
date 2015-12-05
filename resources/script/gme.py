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
import csv
import argparse
import github_email
import time
import random
import math


def read(input_file):
    csv_list = []
    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            csv_list.append(row)
    return csv_list


def write(outputfile, output):
    with open(outputfile, 'a', newline='') as fp:
        writer = csv.writer(fp, delimiter=',')
        writer.writerows(output)


#    ##     ##    ###    ######## ##     ##
#    ###   ###   ## ##      ##    ###    ##
#    #### ####  ##   ##     ##    ####   ##
#    ## ### ## #########    ##    ## ### ##
#    ##  #  ## ##     ##    ##    ##   ####
#    ##     ## ##     ##    ##    ##    ###
#    ##     ## ##     ## ######## ##     ##
##########################################################################
"""
def main(args=None):
	parser = argparse.ArgumentParser(description="Retrieve...)
	parser.add_argument("input", nargs=1, help="The input file")
	parser.add_argument("output", nargs=1, help="The output file)
	args = parser.parse_args()
    print(argz.input[0])
    ret = read(args.input[0])
    for item in ret:
        item.append(github_email.get_github_email(item[2]))
    write(args.output[0], ret)
"""
if __name__ == "__main__":
    # main()
    ret = read("output_users_0-9.csv")
    for item in ret:
        time.sleep(math.fabs(random.gauss(1, 0.5)))
        print(item[2]+".")
        item.append(github_email.get_github_email(item[2]))
    write("list_0-9.csv", ret)
