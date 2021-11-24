#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-11-23
Purpose: Rock the Casbah
"""

import argparse
import sys
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        help='A named string argument',
                        metavar='PATTERN',
                        type=str,
                        default='')

    parser.add_argument('file',
                        help='input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+', default=None)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        type=str, choices='',
                        default=False)

    parser.add_argument('-o',
                        '--outfile', metavar='FILE',
                        help='Output',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
