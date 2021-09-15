#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-09-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Sum numbers',
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
    strings = [str(n) for n in items]

    if args.sorted:
        items.sort()

    bringing = ''
    if num == 1:
        bringing = strings[0]
        print(''+strings[0] + ' = ' +strings[0])
    elif num == 2:
        bringing = ' + '.join(strings)
        print(' + '.join(strings) + ' = ' + str(sum(items)))
    else:
        items[-1] = + items[-1]
        bringing = ' + '.join(strings)
        print('{}'.format(bringing) + ' = ' + str(sum(items)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
