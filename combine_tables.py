#!/usr/bin/env python

'''
author: scott w olesen (swo@mit.edu)

combine two otu tables, etc.
'''

import pysurvey as ps, numpy as np, pandas as pd
import argparse

if __name__ == '__main__':
	p = argparse.ArgumentParser(description='get medians')
	p.add_argument('table1', help='input otu table')
	p.add_argument('table2', help='other input otu table')
	p.add_argument('out', help='output table')
	args = p.parse_args()

	# read tables. don't transpose, since that would cause joining samples, not OTU IDs
	table1 = ps.read_txt(args.table1, verbose=False, T=False)
	table2 = ps.read_txt(args.table2, verbose=False, T=False)

	table = table1.join(table2, how='outer').fillna(0)

	ps.write_txt(table, args.out, T=False)