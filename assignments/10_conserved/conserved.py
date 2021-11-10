#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-11-09
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs = args.file.read().split()
    print("\n".join(seqs))
    for i in range(len(seqs[0])):
        bases = []
        for seq in seqs:
            bases += seq[i]
        common = all(x == bases[0] for x in bases)
        if common:
            print("|", end='')
        else:
            print("X", end='')
    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
