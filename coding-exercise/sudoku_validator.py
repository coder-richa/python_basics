"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from typing import List



def is_valid_row(row: List[str]) -> bool:
    """ Determine if a row is valid.
    :param row: List[str]
    :return: bool
    """

    # Validate row length
    if len(row) != 9:
        return False
    
    
    # Create a set to hold the digits in the row.
    digits = set()
    count_numbers = 0
        
    # Loop through the row.
    for digit in row:
        # If the digit is valid number, add it to the set.
        if digit != '.':
            digits.add(digit)
            count_numbers += 1    

    # If the set has a length of 9, it is valid.
    return len(digits) == count_numbers


def is_valid_column(board: List[List[str]], column: int) -> bool:
    digits = set()
    count_numbers = 0
    for i  in range(9):
        if board[i][column] != '.':
            digits.add(board[i][column])
            count_numbers += 1
    # If the set has a length of 9, it is valid.
    return len(digits) == count_numbers

def is_valid_sub_box(board: List[List[str]], sub_box_number: int) -> bool:
    
    row_start = (sub_box_number // 3) * 3
    col_start = (sub_box_number % 3) * 3
    digits = set()
    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if board[row][col] != '.':
                if board[row][col] in digits:
                    return False
                digits.add(board[row][col])
            
    return True


def is_valid_sudoku(board: List[List[str]]) -> bool:
    """ Determine if a 9 x 9 Sudoku board is valid.
    :param board: List[List[str]]
    :return: bool
    """
    
    # Check if each row is valid.
    for row in board:
        if not is_valid_row(row):
            return False
    
    # Check if each column is valid.
    for column in range(9):
        if not is_valid_column(board, column):
            return False
    
    # Check if each 3x3 sub-box is valid.
    for sub_box in range(9):
        if not is_valid_sub_box(board, sub_box):
            return False
    
    return True

def main():
    
    board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print(is_valid_sudoku(board))
    
if __name__ == '__main__':
    main()