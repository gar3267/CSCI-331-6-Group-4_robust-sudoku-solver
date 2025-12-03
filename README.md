# CSCI-331-6 Group 4 Sudoku Solvers
## Abstract:
Semester long group project in intro to AI in which we created multiple Sudoku solving algorithms to analyze and compare them to one another.
Upon running you aere given a simple PTUI to unit test the board class, or run the search algorithms which gives you the amount of time it took and the backtracking steps it took. This testing is ran on every .sud file found within the code/src/sudoku_boards folder.

## Developers:
Garett (Gayle) Rogers: Worked on PTUI, system to coordinate and collect and print data on running of sudoku algorithms. Also implemented the board class and created the .sud file format.

Veronika K: Created the basic pruning algorithm, and validate choice method for the backtracking algorithm.

Mate: Created the forward checking algorithm.

## How to Run:
Inside the code folder you need to run the "sudokuSolverRunner.py" file. Upon running you will be given 4 choices, 2 of them are for board unit testing, 1 is quit, and 1 is to run the sudoku algorithms. Do beware that there is no timeout and when you get to the basic backtrack you will most likely need to terminate the program.
If you wish to see how the solvers perform on different sudoku boards you can create your own .sud file. The first line is the lexicon the length needs to be a perfect square (this perfect square will now be refered to as n), then you will have n lines each with n characters on them. The characters you may use are within your given lexicon, or a space to designate an empty.

## Problem Description: 
Implement a solver for a Customized Sudoku Puzzle using constraint satisfaction techniques. The base rules of Sudoku apply that each row, column, and region must contain all digits without repetition. Implement and use two algorithms: (1) plain backtracking search and (2) backtracking enhanced with CSP methods such as forward checking or arc consistency

Also, report the difference in efficiency between the two algorithms and explain why the CSP-enhanced version performs better.

## Development Pipeline :
1 - Sudoku board creation
- Create a function that can create different sudoku puzzles, once given a specific lexicon.
- Create a function that parses a file to read a specific sudoku puzzle.
- Unit test this class.

2 - Program Caller
- Determines what functions we are using, what files we're reading.
- Will be done through a PTUI.

3 - Sudoku Solvers
- Impliment the basic backtracking DFS, DFS with pruning enhancements, and DFS with forwarch checking.