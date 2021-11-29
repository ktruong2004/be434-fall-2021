""" Tests for sudoku.py """

import os
from subprocess import getstatusoutput
import re

PRG = './sudoku.py'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_input_1():
    """ Test Input 1"""

    
