"""
LeetCode 0036 – Valid Sudoku

URL: https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import List

import pytest

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validate a partially filled Sudoku board.
        
        Uses three 2D arrays to track seen numbers in rows, columns, and 3x3 sub-boxes.
        For each cell, checks if the number has already been seen in its row, column, or sub-box.
        
        Args:
            board: 9x9 Sudoku board where empty cells are represented by '.'
            
        Returns:
            True if the board is valid according to Sudoku rules, False otherwise
        """
        # Track which numbers (0-8 representing '1'-'9') have been seen in each row, column, and sub-box
        row_has = [[False] * 9 for _ in range(9)]      # row_has[i][x] tracks if number x+1 is in row i
        col_has = [[False] * 9 for _ in range(9)]      # col_has[j][x] tracks if number x+1 is in column j
        sub_box_has = [[[False] * 9 for _ in range(3)] for _ in range(3)]  # sub_box_has[i'][j'][x] tracks if number x+1 is in sub-box (i',j')

        # Iterate through each cell in the board
        for i, row in enumerate(board):
            for j, cell_value in enumerate(row):
                # Skip empty cells
                if cell_value == '.':
                    continue
                    
                # Convert character '1'-'9' to index 0-8
                num_index = int(cell_value) - 1
                
                # Check if this number has already been seen in current row, column, or sub-box
                if (row_has[i][num_index] or 
                    col_has[j][num_index] or 
                    sub_box_has[i // 3][j // 3][num_index]):
                    return False  # Duplicate found, invalid Sudoku
                
                # Mark this number as seen in row, column, and sub-box
                row_has[i][num_index] = True
                col_has[j][num_index] = True
                sub_box_has[i // 3][j // 3][num_index] = True

        return True  # No duplicates found, valid Sudoku


@pytest.mark.parametrize("board, expected", [
    (
        [  # Valid Sudoku board
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        True
    ),
    (
        [  # Invalid Sudoku board (duplicate 8 in top-left 3x3 box)
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ],
        False
    ),
])
def test_solutions(board, expected):
    """Test the isValidSudoku function with valid and invalid Sudoku boards."""
    sol = Solution()
    assert sol.isValidSudoku(board) == expected