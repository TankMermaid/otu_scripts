#!/usr/bin/env python

'''
author: scott w olesen (swo@mit.edu)

convert relative abundances to log10
'''

import pysurvey as ps, numpy as np, pandas as pd
import argparse

if __name__ == '__main__':
	p = argparse.ArgumentParser(description='convert to log10')
	p.add_argument('table', help='input otu table')
	p.add_argument('-o', '--output', help='output table')
	p.add_argument('-z', '--zero', type=float, default=10.0, help='zero values become what negative log? (default: 10)')
	args = p.parse_args()

	new_zero = 10.0 ** (-args.zero)

	table = ps.read_txt(args.table, verbose=False)
	table.replace(to_replace=0.0, value=new_zero, inplace=True)
	logs = table.applymap(np.log10)
	ps.write_txt(logs, args.output, verbose=False)