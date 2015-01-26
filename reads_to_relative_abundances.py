#!/usr/bin/env python

'''
reads_to_relative_abundances.py

author: scott w olesen (swo@mit.edu)

goes from counts to relative abundances
'''

import pandas as pd, numpy as np
import argparse

if __name__ == '__main__':
	p = argparse.ArgumentParser(description='counts to relative abundances')
	p.add_argument('table', help='input otu table')
	p.add_argument('out', help='output otu table')
	#p.add_argument('-p', '--pseudo', type=int, help='add pseudocounts?')
	args = p.parse_args()

	# read in table
	table = pd.read_table(args.table, index_col=0)

    norm = table.apply(lambda col: col.astype(float) / np.sum(col), axis=0)
    norm.to_csv(args.out, sep='\t')
