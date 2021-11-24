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
                        help='Search Pattern',
                        metavar='PATTERN')

    parser.add_argument('file',
                        help='input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true',
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
    num_files = len(args.file)

    for fh in args.file:
        for line in fh:
            if re.search(args.pattern, line,
            re.IGNORECASE if args.insensitive else 0):
                args.outfile.write('{}{}'.format(
                    f'{fh.name}:' if num_files > 1 else '', line))


# --------------------------------------------------
if __name__ == '__main__':
    main()
