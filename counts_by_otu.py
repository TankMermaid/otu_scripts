#!/usr/bin/env python

'''
author: scott w olesen (swo@mit.edu)
'''

import numpy as np, pandas as pd
import argparse, sys

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='get counts in each otu')
    p.add_argument('table', help='input otu table')
    p.add_argument('-o', '--output', default=sys.stdout, type=argparse.FileType('w'), help='output file (default stdout)')
    args = p.parse_args()

    table = pd.read_table(args.table, index_col=0).transpose()
    sums = table.apply(np.sum)

    for name, val in sums.iteritems():
        args.output.write("{}\t{}\n".format(name, val))
