""" Tests for sudoku.py """

# pylint:disable=consider-using-with,unspecified-encoding

import os
from subprocess import getstatusoutput
import random
import re
import string

PRG = './sudoku.py'


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
