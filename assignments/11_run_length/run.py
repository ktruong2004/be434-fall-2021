#!/usr/bin/env python3
"""
Author : ktruong <ktruong@localhost>
Date   : 2021-11-16
Purpose: Rock the Casbah
"""

import argparse
import os
from collections import OrderedDict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='DNA text or file',
                        metavar='str',
                        type=str)


    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for seq in args.text.splitlines():
        print(rle(seq))


# --------------------------------------------------
def encode(rle):
    """ Create RLE """

    encoded_message = ""
    i = 0
    while (i <= len(rle)-1):
        count = 1
        ch = rle[i]
        j = i
        while (j < len(rle)-1):
            if (rle[j] == rle[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_message = encoded_message+str(count)+ch
        i = j+1
    return encoded_message


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'
# --------------------------------------------------
if __name__ == '__main__':
    main()
