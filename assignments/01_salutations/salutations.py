#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-09-02
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        default='Stranger')

 
    parser.add_argument('-e',
                        '--excited',
                        help='A boolean flag',
                        action='store_true', default= False)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    if args.excited:
        print(f'{args.greeting}, {args.name}!')
    else:
        print(f'{args.greeting}, {args.name}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
