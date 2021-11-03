#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-11-02
Purpose: Rock the Casbah
"""

import argparse
import os
from Bio import SeqIO
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    
    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs="+",
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        type=argparse.FileType('w'),
                        default="split")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    reader = SeqIO.parse('inputs/reads1.fa', 'fasta')
    for rec in reader:
        print('ID :', rec.id)
        print('Seq:', str(rec.seq))
# --------------------------------------------------
if __name__ == '__main__':
    main()
