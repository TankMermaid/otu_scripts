#!/usr/bin/env python

'''
author: scott w olesen (swo@mit.edu)
'''

import pysurvey as ps, numpy as np, pandas as pd
import argparse, sys

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='get counts in each otu')
    p.add_argument('table', help='input otu table')
    p.add_argument('-o', '--output', default=sys.stdout, type=argparse.FileType('w'), help='output file (default stdout)')
    args = p.parse_args()

    table = ps.read_txt(args.table, verbose=False, T=True)
    sums = table.apply(np.sum).values
    for s in sums:
        print s
