""" Tests for sudoku.py """

# pylint:disable=consider-using-with,unspecified-encoding

import os
from subprocess import getstatusoutput
import random
import re
import string

PRG = './sudoku.py'


# --------------------------------------------------
def random_filename():
    """ Generate a random filename """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """fails on bad input"""

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} foo {bad}')
    assert rv != 0
    assert re.search(f"error: unrecognized arguments: foo {bad}", out)


# --------------------------------------------------
def run(input_seq, codons, expected):
    """ Run """

    random_file = random_filename()
    try:
        flip = random.randint(0, 1)
        out_file, out_arg = (random_file,
                             '-o ' + random_file) if flip == 1 else ('out.txt',
                                                                     '')
        print(f'{PRG} -c {codons} {out_arg} {input_seq}')
        rv, output = getstatusoutput(
            f'{PRG} -c {codons} {out_arg} {input_seq}')

        assert rv == 0
        assert output.rstrip() == f'Output written to "{out_file}".'
        assert os.path.isfile(out_file)
        with open(out_file, encoding='utf-8') as fh:
            assert fh.read().strip() == expected
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)
