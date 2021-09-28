#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-09-27
Purpose: Rock the Casbah
"""

import argparse
import io

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',type=argparse.FileType('rt'),
                        metavar ='FILE',nargs='+',default=None)

    parser.add_argument('-n','--number',
                        help='Number the lines',
                        type=int,nargs='+',
                        default=False)


    args = parser.parse_args()


    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    
    args = get_args()
    for fh in args.file:
        for line_number, line in enumerate(fh, start=1):
            if args.number:
                print(line_number   ,line,end='')
            else:
                print(line,end='')
    
 




# --------------------------------------------------
if __name__ == '__main__':
    main()
