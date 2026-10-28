import numpy as np
import itertools

class Board:
    def __init__(self, puzzle):
        self.arr = self.string_puzzle_to_arr(puzzle)
    
    def get_row(self, row_index):
        return self.arr[row_index]

    def get_column(self, col_index):
        return self.arr.T[col_index]

    def get_block(self, pos_1, pos_2):
        return self.arr[pos_1 * 3: (pos_1 * 3) + 3, pos_2 * 3: (pos_2 * 3) + 3]

    def iter_rows(self):
        return self.arr

    def iter_columns(self):
        return self.arr.T

    def iter_blocks(self):
        return [self.arr[pos_1 * 3: (pos_1 * 3) + 3, pos_2 * 3: (pos_2 * 3) + 3] for pos_1 in range(3) for pos_2 in range(3)]

    def string_puzzle_to_arr(self,line):
        return np.array([int(num) for num in line.strip()]).reshape(9,9)
    

# Part 2:
def is_subset_valid(arr):
    return bool(len(set(arr.flatten())) + max(((arr == 0).sum() - 1),0) == len(arr.flatten()))


def is_valid(board):
    rows = board.iter_rows()
    columns = board.iter_columns()
    blocks = board.iter_blocks()

    for subset in itertools.chain(rows,columns,blocks):
        if is_subset_valid(subset):
            continue
        else: return False
 
    return True

# Part 3:
def find_empty(board):
    solutions = []
    for idx,element in np.ndenumerate(board.arr):
        if element == 0:
            solutions.append(idx)
    
    if(len(solutions) == 0 ): return None
    return np.array([element for element in solutions])

def is_full(board):
    return find_empty(board) is None

def find_possibilities(board, x, y):
    block_pos = x // 3, y // 3
    row = board.get_row(x)
    column = board.get_column(y)
    block = board.get_block(*block_pos).flatten()
    return [num for num in range(1,10) if not (num in itertools.chain(row,column,block))]