# Sudoku-Solver

Create a Python program called `sudoku.py` that will solve a sudoku puzzle.
In the sudoku puzzle, players will insert the numbers one to nine into a grid consisting of nine squares subdivided into a further nine smaller squares in such a way that every number appears once in each horizontal line, vertical line, and square.
This program will solve sudoku puzzles using a backtracking algorithm. It will visit the empty cells in some order.Each cell is tested for a valid number, moving "back" when there is a violation, and moving forward again until the puzzle is solved.

Here is the usage the program should print for `-h` or `--help`:

```
$ ./sudoku.py -h
usage: tictactoe.py [-h] [-b str] [-p str] [-c int]

usage: sudoku.py [-h] [-o FILE]

Rock the Casbah

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --outfile FILE
                        Output filename (default: out.txt)
```

Players will need to fill the sudoku puzzle into the "input_sudoku" variable according to order. In this program the empty cells have assigned with 0.
When players fill a valid sudoku puzzle:

```
$ ./sudoku.py
Here is the solver:
 ┎─────────────────────────────┒
 ┃  7 1 8  ┃  9 5 2  ┃  3 4 6  ┃
 ┃  4 5 3  ┃  6 7 1  ┃  2 8 9  ┃
 ┃  2 6 9  ┃  4 8 3  ┃  5 1 7  ┃
 ┠─────────────────────────────┨
 ┃  3 9 1  ┃  5 2 6  ┃  8 7 4  ┃
 ┃  6 8 2  ┃  3 4 7  ┃  1 9 5  ┃
 ┃  5 4 7  ┃  8 1 9  ┃  6 2 3  ┃
 ┠─────────────────────────────┨
 ┃  1 3 5  ┃  7 9 8  ┃  4 6 2  ┃
 ┃  9 2 4  ┃  1 6 5  ┃  7 3 8  ┃
 ┃  8 7 6  ┃  2 3 4  ┃  9 5 1  ┃
 ┖─────────────────────────────┚
```

When players fill an invalid sudoku puzzle:

```
$ ./sudoku.py 
--------------------------------------

Something is wrong. Please check your sudoku again!!!
```

Finally, the program should print all output the `-o|--output` which should default to `out.txt`:

```
$ ./sudoku.py -o testing.txt

```

The program should pass all tests:

```
$ make test
pytest -xv test.py
============================= test session starts ==============================
...
collected 7 items

test.py::PYLINT PASSED                                                                                                                                                                                  [ 14%]
test.py::FLAKE8 PASSED                                                                                                                                                                                  [ 28%]
test.py::test_exists PASSED                                                                                                                                                                             [ 42%]
test.py::test_usage PASSED                                                                                                                                                                              [ 57%]
test.py::test_bad_file PASSED                                                                                                                                                                           [ 71%]
sudoku.py::PYLINT SKIPPED (file(s) previously passed pylint checks)                                                                                                                                     [ 85%]
sudoku.py::FLAKE8 SKIPPED (file(s) previously passed FLAKE8 checks)                                                                                                                                     [100%]

======================================================================================== 5 passed, 2 skipped in 1.02s =========================================================================================
```
