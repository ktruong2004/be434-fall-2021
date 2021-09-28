#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-09-27
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
                        help='Input file(s)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+', default=None)

    parser.add_argument('-n', '--number', help='Number the lines',
                        action='store_true', default=False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.file:
        for line_number, line in enumerate(fh, start=1):
            if args.number:
                print("     {}	{}".format(line_number, line), end='')
            else:
                print(f'{line}', end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
