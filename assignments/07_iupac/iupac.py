#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-10-18
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seqs',
                        help='Input sequence(s)',
                        metavar='SEQ', nargs='+')

    parser.add_argument('-o',
                        '--outfile', metavar='FILE',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    iupac = {'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T', 'U': 'U',
             'R': '[AG]', 'S': '[GC]', 'W': '[AT]', 'K': '[GT]',
             'M': '[AC]', 'Y': '[CT]', 'B': '[CGT]', 'D': '[AGT]',
             'H': '[ACT]', 'V': '[ACG]', 'N': '[ACGT]'}
    for char in args.seqs:
        print(char, char.translate(str.maketrans(iupac)), file=args.outfile)
    if args.outfile != sys.stdout:
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
