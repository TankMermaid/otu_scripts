#!/usr/bin/env python

'''
author: scott w olesen (swo@mit.edu)

this script filters otus based on their median abundance across all samples
'''

import pysurvey as ps, numpy as np
import argparse

if __name__ == '__main__':
	p = argparse.ArgumentParser(description='filter otus based on their median abundance')
	p.add_argument('table', help='input otu table')
	p.add_argument('out', help='output otu table')
	g = p.add_mutually_exclusive_group(required=True)
	g.add_argument('-l', '--log', type=float, help='minimum median (negative log10)')
	g.add_argument('-m', '--min', type=float, help='minimum median (raw value)')
	args = p.parse_args()

	# load up the table
	table = ps.read_txt(args.table)

	# convert to raw minimum median
	if args.log:
		args.min = 10.0 ** (-args.log)

	print "comparing medians to {}".format(args.min)

	# filter columns if the median is below the specified min
	criterion = (lambda x: np.median(x), lambda x,y: x>y, args.min)
	table = ps.filter_by_vals(table, criterion)

	# write out the filtered table
	ps.write_txt(table, args.out)