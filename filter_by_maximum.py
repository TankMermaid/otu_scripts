#!/usr/bin/env python

'''
author: scott w olesen (swo@mit.edu)
'''

import pysurvey as ps, numpy as np
import argparse

if __name__ == '__main__':
	p = argparse.ArgumentParser(description='filter otus based on their maximum abundance')
	p.add_argument('table', help='input otu table')
	p.add_argument('-o', '--output', help='output otu table', required=True)
	g = p.add_mutually_exclusive_group(required=True)
	g.add_argument('-l', '--log', type=float, help='minimum max (negative log10)')
	g.add_argument('-m', '--min', type=float, help='minimum max (raw value)')
	args = p.parse_args()

	# load up the table
	table = ps.read_txt(args.table)

	# convert to raw minimum median
	if args.log:
		args.min = 10.0 ** (-args.log)

	# filter columns if the maximum is below the specified min
	criterion = (np.max, lambda x,y: x>y, args.min)
	table = ps.filter_by_vals(table, criterion)

	# write out the filtered table
	ps.write_txt(table, args.output)
