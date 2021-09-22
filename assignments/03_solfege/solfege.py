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
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='A named string argument',
                        metavar='str',nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    answers = { 'Do' : 'Do, A deer, a female deer', 
                'Re' : 'Re, A drop of golden sun',
                'Mi': 'Mi, A name I call myself',
                'Fa' : 'Fa, A long long way to run',
                'Sol' : 'Sol, A needle pulling thread',
                'La' : 'La, A note to follow sol',
                'Ti' : 'Ti, A drink with jam and bread'}

    
    for char in args.text:
        if char in answers:
            print(answers[char])
        else:
            print(f'I don\'t know "{char}"')

    
       
# --------------------------------------------------
if __name__ == '__main__':
    main()
