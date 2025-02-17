#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-09-20
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='A named string argument',
                        metavar='str')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {'1' : '9', '2' : '8', '3' : '7', '4': '6',
            '5' : '0', '6' : '4', '7' : '3', '8': '2', '9': '1'}
   
    for char in args.text:
        if char in jumper:
            print(jumper[char], end='')
        else:
            print( char, end='')
    print()
    
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
