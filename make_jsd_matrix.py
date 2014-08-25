#!/usr/bin/env python

'''
author: scott w olesen (swo@mit.edu)
'''

import pysurvey as ps, numpy as np, pandas as pd
import argparse

if __name__ == '__main__':
	p = argparse.ArgumentParser(description='make a jsd matrix')
	p.add_argument('table', help='normalized otu table')
	p.add_argument('out', help='output matrix')
	args = p.parse_args()

	table = ps.read_txt(args.table, verbose=False)
	mat = ps.dist_mat(table, metric='JS')

	ps.write_txt(mat, args.out)
