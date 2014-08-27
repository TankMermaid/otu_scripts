#!/usr/bin/env python

import argparse, pysurvey as ps, pandas as pd, numpy as np
import sys

def shannon(x):
    y = np.array(x, dtype=float)
    y = y[y > 0]    # get nonzero values
    #y /= np.sum(y)  # convert to rel abund
    return -np.sum(y * np.log2(y))

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('table', help='input otu table')
    p.add_argument('-o', '--output', default=sys.stdout, type=argparse.FileType('w'), help='output file (default stdout)')
    args = p.parse_args()

    table = ps.read_txt(args.table, verbose=False)

    shannon_vals = table.apply(shannon, axis=1)
    np.savetxt(args.output, shannon_vals)