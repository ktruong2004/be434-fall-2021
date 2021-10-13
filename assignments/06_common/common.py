#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-10-06
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile', metavar='FILE',
                        help='A boolean flag',
                        type=argparse.FileType('wt'),
                        default="out.txt")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file1 = args.FILE1
    file2 = args.FILE2
    word1 = {}
    word2 = {}
    for fh in file1:
        for line1 in fh.split():
            if line1 not in word1.keys():
                word1[line1] = 0
            word1[line1] += 1
        for gh in file2:
            for line2 in gh.split():
                if line2 not in word2.keys():
                    word2[line2] = 0
                word2[line2] += 1
    setA = set(word1)
    setB = set(word2)
    setA.intersection(setB)
    for item in setA.intersection(setB):
        print(item)


# --------------------------------------------------
if __name__ == '__main__':
    main()
