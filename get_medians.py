#!/usr/bin/env python

'''
author: scott w olesen (swo@mit.edu)

this script grabs medians from an otu table
'''

import pysurvey as ps, numpy as np, pandas as pd
import argparse

if __name__ == '__main__':
	p = argparse.ArgumentParser(description='get medians')
	p.add_argument('table', help='input otu table')
	p.add_argument('out', help='output medians list')
	args = p.parse_args()

	table = ps.read_txt(args.table, verbose=False)
	medians = pd.DataFrame({'median': table.apply(np.median)}).T
	ps.write_txt(medians, args.out)