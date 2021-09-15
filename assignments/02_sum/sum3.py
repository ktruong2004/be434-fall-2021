#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-09-13
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sum Numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('nums',
                        metavar='int',
                        type=int,
                        nargs='+',
                        help='Numbers to add')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
    numbers: list[int] = args.nums
    nums = [str(num) for num in args.nums]
    print('{} = {}'.format(' + '.join(map(str, args.nums)), sum(args.nums)))


# --------------------------------------------------
if __name__ == '__main__':
    main()