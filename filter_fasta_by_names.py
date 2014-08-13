#!/usr/bin/env python

'''
author: scott w olesen (swo@mit.edu)
'''

from Bio import SeqIO
import argparse, sys

if __name__ == '__main__':
	p = argparse.ArgumentParser(description='get only fasta entries with ids in some list')
	p.add_argument('ids', help='input ids file')
	p.add_argument('fasta', help='input fasta')
	p.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout, help='output fasta')
	args = p.parse_args()

	# read in the names
	with open(args.ids) as f:
		ids = [line.strip() for line in f]

	# get the fasta lines
	for record in SeqIO.parse(args.fasta, 'fasta'):
		if record.id in ids:
			SeqIO.write(record, args.output, 'fasta')