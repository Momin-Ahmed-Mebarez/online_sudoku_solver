import numpy as np
import itertools

#The sudoku puzzle is used to create A Board object
class Board:
    def __init__(self, puzzle: str):
        self.arr = self.string_puzzle_to_arr(puzzle)
    
    def get_row(self, row_index: int) -> np.ndarray:
        return self.arr[row_index]

    def get_column(self, col_index: int) -> np.ndarray:
        return self.arr.T[col_index]
    #Pos_1, Pos_2 are based on the cords of the top-left corner in a block (the default 9 blocks).
    def get_block(self, pos_1: int, pos_2: int) -> np.ndarray:
        return self.arr[pos_1 * 3: (pos_1 * 3) + 3, pos_2 * 3: (pos_2 * 3) + 3]

    def iter_rows(self) -> np.ndarray:
        return self.arr

    def iter_columns(self) -> np.ndarray:
        return self.arr.T

    def iter_blocks(self) -> np.ndarray:
        return [self.arr[pos_1 * 3: (pos_1 * 3) + 3, pos_2 * 3: (pos_2 * 3) + 3] for pos_1 in range(3) for pos_2 in range(3)]
    #The puzzle is passed as a block of text where each line is a full row
    def string_puzzle_to_arr(self,line: str) -> np.ndarray:
        return np.array([int(num) for num in line.strip()]).reshape(9,9)
    

#Healper methods

# Part 2:
#We pass a single row, column or block then the function checks that all the numbers are unique
def is_subset_valid(arr: np.ndarray) -> bool:
    #We use flatten to support blocks.
    #-We cast the array into set to remove duplicates then calculate it's length
    #Since the duplicate zero's are removed we recalculate their total and add it to the length. 
    #-We compare the length of the generated set with the original array length
    #-If a duplicate was removed the legnths won't match
    return bool(len(set(arr.flatten())) + max(((arr == 0).sum() - 1),0) == len(arr.flatten()))

#Checks the entire board to make sure the solution is valid
def is_valid(board: Board) -> bool:
    rows = board.iter_rows()
    columns = board.iter_columns()
    blocks = board.iter_blocks()
    #Chain creates a big list of all our rows,columns and blocks
    for subset in itertools.chain(rows,columns,blocks):
        if is_subset_valid(subset):
            continue
        else: return False
 
    return True

# Part 3:
#Searchs for empty cells (the value inside the cell is 0)
def find_empty(board: Board) -> np.ndarray:
    empty_cell = []
    for idx,cell in np.ndenumerate(board.arr):
        if cell == 0:
            empty_cell.append(idx)
    
    if(len(empty_cell) == 0 ): return None
    return np.array([cell for cell in empty_cell])
#Checks if the board have no more empty cells 
def is_full(board: Board) -> bool:
    return find_empty(board) is None
#Checks the possible solutions for a cell
def find_possibilities(board: Board, x: int, y: int) -> list:
    block_pos = x // 3, y // 3
    row = board.get_row(x)
    column = board.get_column(y)
    block = board.get_block(*block_pos).flatten()
    #Creates a list of numbers form 1,9 if the number is unique in it's row,column and block
    return [num for num in range(1,10) if not (num in itertools.chain(row,column,block))]