#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-10-04
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

    parser.add_argument('file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='*',default=[sys.stdin])

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    for fh in args.file:
        total_lines = 0
        total_words = 0
        total_chars = 0
        num_lines = 0
        num_words = 0
        num_chars = 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_chars += len(line)

        total_lines += num_lines
        total_words += num_words
        total_chars += num_chars


        print(f'{num_lines:8}{num_words:8}{num_chars:8} {fh.name}')

    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_chars:8} total')



# --------------------------------------------------
if __name__ == '__main__':
    main()
