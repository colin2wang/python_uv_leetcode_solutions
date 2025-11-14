"""
LeetCode 0006 – Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

This solution simulates the zigzag traversal by moving a pointer up and down the rows,
appending each character to the corresponding row string.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for storing the result strings

URL: https://leetcode.com/problems/zigzag-conversion/
"""
import pytest

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert a string to zigzag pattern and read line by line.
        
        Args:
            s (str): Input string
            numRows (int): Number of rows for zigzag pattern
            
        Returns:
            str: String read line by line from zigzag pattern
            
        Example:
            >>> sol = Solution()
            >>> sol.convert("PAYPALISHIRING", 3)
            "PAHNAPLSIIGYIR"
        """
        # Edge case: if only one row, return original string
        if numRows == 1 or numRows >= len(s):
            return s
            
        # Create list to store characters for each row
        rows = [''] * numRows
        
        # Current row index and direction step (+1 for down, -1 for up)
        row, step = 0, 1

        # Traverse each character and place it in the appropriate row
        for c in s:
            rows[row] += c
            
            # Change direction when reaching top or bottom row
            if row == 0:
                step = 1  # Move downward
            elif row == numRows - 1:
                step = -1  # Move upward
                
            row += step  # Move to next row

        # Concatenate all rows to get final result
        return ''.join(rows)

@pytest.mark.parametrize("s, numRows, expected", [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A"),
])
def test_solutions(s, numRows, expected):
    sol = Solution()
    assert sol.convert(s, numRows) == expected