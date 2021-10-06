#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-10-04
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        help='DNA/RNA sequence',
                        type=str)

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default= 'out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    codon_table = {}
    for line in args.codons:
        key, value = line.strip().split()
        codon_table[key] = value
    # pprint(codon_table)

    k = 3
    seq = args.sequence.upper()
    for codon in [seq[i:i + k] for i in range(0,len(seq),k)]:
        print(codon_table.get(codon,'-'),end='',file=args.outfile)

    print(file=args.outfile)
    print(f'Output written to "{args.outfile.name}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
