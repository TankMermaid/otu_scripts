#!/usr/bin/env python

import argparse
import numpy as np
import sys

parser = argparse.ArgumentParser(description="Column- or row-normalize (or both) a table.")
parser.add_argument('input_table', type=str, help='input OTU table')
parser.add_argument('-o', '--output', metavar='FILE', type=argparse.FileType('w'), default=sys.stdout, help='output file (default: print to standard output)')
parser.add_argument('axes', type=int, metavar='axis', nargs='+', default=0, help='axis (or axes) over which to normalize (0=column [default]; 1=row; 0 1=by column then by row)')

args = parser.parse_args()

table = np.genfromtxt(args.input_table)

for axis in args.axes:
    if axis == 0:
        table /= table.sum(axis=0)[np.newaxis, :]
    elif axis == 1:
        table /= table.sum(axis=1)[:, np.newaxis]

np.savetxt(args.output, table, delimiter='\t')
