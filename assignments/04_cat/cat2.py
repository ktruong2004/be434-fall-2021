#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-09-29
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

    # args = parser.parse_args()
    
    # if not 3 <= len(args.file) <= 5:
    #     parser.error('Must have 3-5 files')
    
    # return args
    return parser.parse_args()


# --------------------------------------------------
def main(): #define function
    """Make a jazz noise here"""

    args = get_args() #define variable

    for fh in args.file:
        line_num = 0
        for line in fh:
            line_num += 1
            if args.number:
                print('{:6}\t{}'.format(line_num,line.rstrip()))
            else:
                print(line,end='')
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
