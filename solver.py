import numpy as np
from sudoku import Board, find_possibilities, is_full, is_valid, find_empty

def solve_sudoku(board: Board):
    if(is_full(board)): 
        if(is_valid(board)):
            return True
        return False

    x,y = find_empty(board)[0]
    
    for possiblity in find_possibilities(board,x,y):
        board.arr[x][y] = possiblity
        if(not is_valid(board)): continue
        if(solve_sudoku(board)): return True
        board.arr[x][y] = 0

def remove_one_solution(board):
    one_guess_solutions_flag = True
    while(one_guess_solutions_flag):
        one_guess_solutions_flag = False
        for x,y in find_empty(board):
            possiblities =  find_possibilities(board,x,y)
            if(len(possiblities) > 1): continue
            board.arr[x][y] = possiblities
            if(is_full(board)):
                one_guess_solutions_flag = False
                break
            one_guess_solutions_flag = True
    if(is_full(board)): return
    else: solve_sudoku(board)

def start(board):
    original = Board(board)
    np_board = Board(board)
    remove_one_solution(np_board)
    return (original.arr.flatten(),np_board.arr.flatten())

