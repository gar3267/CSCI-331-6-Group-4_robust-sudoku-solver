import src.sudokuSearch as sudokuSearch
from src.sudokuBoard import Board
import os
import csv

def testBoard(withUser=False):
    board0:Board = Board(lexicon=['a','b','c'],board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
    print(board0)
    validity:str = board0.validate()
    print(validity)
    if validity is None:
        print('============================\nVALIDITY SHOULD HAVE FAILED\n============================')

    board1:Board
    with open('src/sudoku_boards/board1.sud','r') as file:
        board1 = Board(file=file)
    print(board1)
    validity = board1.validate()
    print(validity)
    if validity is None:
        print('============================\nVALIDITY SHOULD HAVE FAILED\n============================')
    
    answer1:Board
    with open('src/sudoku_boards/answers/answer1.sud','r') as file:
        answer1 = Board(file=file)
    print('\n'+str(answer1))
    validity = answer1.validate()
    print(validity)
    if validity is not None:
        print("==============================\nVALIDITY SHOULDN'T HAVE FAILED\n==============================")
    
    # Testing validity
    badValidBoards:list[tuple[Board,str]] = getBoardsFromFolder('src/sudoku_boards/bad_boards')
    for board in badValidBoards:
        print('\n'+str(board[1])+'\n'+str(board[0]))
        validity = board[0].validate()
        print(validity)
        if validity is None:
            print('============================\nVALIDITY SHOULD HAVE FAILED\n============================')

    # Testing user input
    if withUser:
        userBoard:Board = Board()
        print(userBoard)
        print(userBoard.validate())
    
    # Adding extra enter
    print()


def getUserBoard():
    """Uses board's init to get a board from user input"""
    return Board()


def getBoardsFromFolder(path:str = 'code/src/sudoku_boards'):
    """Gets all the boards pathin sudoku_boards folder then returns them as list"""
    dir_list = os.listdir(path)
    result:list[tuple[Board,str]] = []

    # If it blows up, that tells you that you did the file wrong
    for filename in dir_list:
        fileBoard:Board
        if filename[-4:] == '.sud':
            with open(path+'/'+filename,'r') as file:
                fileBoard = Board(file=file)
                result.append((fileBoard,filename))
    
    return result


def testSearchAlgorithms():
    # Testing with forward checking
    print('Testing with forward checking algorithm.')
    testBoards = getBoardsFromFolder()
    for board in testBoards:
        print('\nTesting ' + str(board[1]))
        count, seconds = sudokuSearch.forwardCheckingSudokuTime(board[0])
        print('\nSolved in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')

    # Testing with pruned
    print('Testing with pruned node expansions.')
    testBoards = getBoardsFromFolder()
    for board in testBoards:
        print('\nTesting '+str(board[1]))
        count, seconds = sudokuSearch.backtrackPrunedSudokuTime(board[0])
        print('\nSolved in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')

    # Testing with backtrack
    print('Testing with basic backtracking algorithm.')
    testBoards = getBoardsFromFolder()
    for board in testBoards:
        print('\nTesting '+str(board[1]))
        count, seconds = sudokuSearch.backtrackSudokuTime(board[0])
        print('\nSolved in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')

def testPruningAlgorithms():
    # Testing with pruned

    board1:Board
    with open('src/sudoku_boards/board_4x4.sud','r') as file: # 16x16.sud','r') as file:
        board1 = Board(file=file)

    print('\nSolving 4x4 Board with Pruning ...\n')

    count, seconds = sudokuSearch.backtrackPrunedSudokuTime(board1)
    print('\nSolved in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')

    """ answer1:Board # CSCI-331-6-Group-4_robust-sudoku-solver/code/src/sudoku_boards/answers/answer_4x4.sud
    with open('src/sudoku_boards/answers/answer_4x4.sud','r') as file:
        answer1 = Board(file=file)
    print('\n'+str(board1.equals(answer1))) """


    # Testing with pruned

    board1:Board
    with open('src/sudoku_boards/board2.sud','r') as file: # 16x16.sud','r') as file:
        board1 = Board(file=file)

    print('\nSolving 9x9 Board with Pruning ...\n')

    count, seconds = sudokuSearch.backtrackPrunedSudokuTime(board1)
    print('\nSolved in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')

    """ answer1:Board
    with open('src/sudoku_boards/answers/answer1.sud','r') as file:
        answer1 = Board(file=file)
    print('\n'+str(board1.equals(answer1))) """





    # Testing with forward

    board1:Board
    with open('src/sudoku_boards/board_4x4.sud','r') as file: # 16x16.sud','r') as file:
        board1 = Board(file=file)

    print('\nSolving 4x4 Board with Forward Checking ...\n')

    count, seconds = sudokuSearch.forwardCheckingSudokuTime(board1)
    print('\nSolved in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')
    print(board1)
    """ 

    answer1:Board
    with open('src/sudoku_boards/answers/answer_4x4.sud','r') as file:
        answer1 = Board(file=file)
    print('\n'+str(board1.equals(answer1))) """


    # Testing with forward

    board1:Board
    with open('src/sudoku_boards/board2.sud','r') as file: # 16x16.sud','r') as file:
        board1 = Board(file=file)

    print('\nSolving 9x9 Board with Forward Checking ...\n')

    count, seconds = sudokuSearch.forwardCheckingSudokuTime(board1)
    print('\nSolved in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')
    print(board1)

    """ answer1:Board
    with open('src/sudoku_boards/answers/answer1.sud','r') as file:
        answer1 = Board(file=file)
    print('\n'+str(board1.equals(answer1))) """

    # run_experiments()
    basic_backtrack()

    
def run_experiments():
    """
    Run pruned backtracking and forward checking on a list of Sudoku boards
    and save results (board name, algorithm, backtracks, runtime) to CSV.
    """

    output_csv='src/sudoku_boards/results.csv'
    results = []
    board_files=[
        'src/sudoku_boards/board_4x4.sud',
        'src/sudoku_boards/board_9x9_1.sud',
        #'src/sudoku_boards/board_9x9_2.sud',
        'src/sudoku_boards/board_9x9_3.sud',
        'src/sudoku_boards/board_9x9_4.sud',
        'src/sudoku_boards/board2.sud'
        ]

    for board_file in board_files:
        # Load board
        with open(board_file, 'r') as f:
            board = Board(file=f)

        board_name = board_file.split("/")[-1]  # just filename for readability

        # --- Pruned Backtracking ---
        count, seconds = sudokuSearch.backtrackPrunedSudokuTime(board)
        results.append([board_name, "Pruned Backtracking", count, seconds])

        # Reload board (since previous run modified it)
        with open(board_file, 'r') as f:
            board = Board(file=f)

        # --- Forward Checking ---
        count, seconds = sudokuSearch.forwardCheckingSudokuTime(board)
        results.append([board_name, "Forward Checking", count, seconds])

    # Write results to CSV
    with open(output_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Board", "Algorithm", "Backtracks", "Runtime (s)"])
        writer.writerows(results)

    print(f"Results written to {output_csv}")


def basic_backtrack() :
    board1:Board
    with open('src/sudoku_boards/board_4x4.sud','r') as file: # 16x16.sud','r') as file:
        board1 = Board(file=file)

    count, seconds = sudokuSearch.backtrackSudokuTime(board1)
    print('\nSolved 4x4 board w/ normal backtracking in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')

    board1:Board
    with open('src/sudoku_boards/board2.sud','r') as file: # 16x16.sud','r') as file:
        board1 = Board(file=file)

    count, seconds = sudokuSearch.backtrackSudokuTime(board1)
    print('\nSolved 9x9 board w/ normal backtracking in ' + str(seconds) + ' seconds with ' + str(count) + ' backtracking steps\n')
