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

import csv, random, sys, argparse

def shuffle_rows(inputfile, outputfile, options={"preserve-header":False}):
	with open(inputfile) as ifile:
		r = csv.reader(ifile)
		header = next(r) if (options["preserve-header"]) else None
		l = list(r)
		random.shuffle(l)

	with open(outputfile, "w") as ofile:
		writer = csv.writer(ofile, delimiter=',')
		if header != None: writer.writerow(header)
		writer.writerows(l)


#    ##     ##    ###    ######## ##     ##
#    ###   ###   ## ##      ##    ###    ##
#    #### ####  ##   ##     ##    ####   ##
#    ## ### ## #########    ##    ## ### ##
#    ##  #  ## ##     ##    ##    ##   ####
#    ##     ## ##     ##    ##    ##    ###
#    ##     ## ##     ## ######## ##     ##
################################################################################

def main(argv):
	parser = argparse.ArgumentParser(description="""Shuffles the rows of a CSV
		file""")

	parser.add_argument("input",nargs=1, help="""The input file""")

	parser.add_argument("output",nargs=1, help="""The output file""")

	parser.add_argument('--header', dest='header', action='store_true',
		help="""If present, the first row will not be shuffled""")
	parser.add_argument('--no-header', dest='header', action='store_false',
		help="""If present, the first row will be shuffled""")
	parser.set_defaults(header=False)

	args = parser.parse_args()
	options = {
		"preserve-header" : args.header
	}

	shuffle_rows(args.input[0],args.output[0], options)




if __name__ == "__main__":
	main(sys.argv[1:])
