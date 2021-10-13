#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-10-13
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

    parser.add_argument('FILE1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile', metavar='FILE',
                        help='A boolean flag',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word1 = args.FILE1.read().split()
    word2 = args.FILE2.read().split()
    # word1 = {}
    # word2 = {}
    for word in word1:
        if word in word2:
            print(word, file=args.outfile)



# --------------------------------------------------
if __name__ == '__main__':
    main()
