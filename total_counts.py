#!/usr/bin/env python

'''
author: scott w olesen (swo@mit.edu)
'''

import pysurvey as ps, numpy as np, pandas as pd
import argparse, sys

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='get total counts across samples and otus')
    p.add_argument('table', help='input otu table')
    p.add_argument('-o', '--output', default=sys.stdout, type=argparse.FileType('w'), help='output file (default stdout)')
    args = p.parse_args()

    table = ps.read_txt(args.table, verbose=False, T=False)
    total = np.sum(table.apply(np.sum))
    print total
