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

    parser.add_argument('item',
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
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()
    if num == 1:
        print(f'{items[0]} = {items[0]}')
    elif num == 2:
        sum1 = items[0] + items[1]
        print(f'{items[0]} + {items[1]} = {sum1}')
    elif num == 3:
        sum2 = items[0] + items[1] + items[2]
        print(f'{items[0]} + {items[1]} + {items[2]} = {sum2}')
    else:
        sum3 = items[0] + items[1] + items[2] + items[3]
        print(f'{items[0]} + {items[1]} + {items[2]} + {items[3]} = {sum3}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
