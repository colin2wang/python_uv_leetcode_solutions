"""
LeetCode 2536 – Increment Submatrices By One

You are given a positive integer n and a list of queries where each query specifies 
a submatrix region. Initially, all cells in an n x n matrix are zero. For each query,
increment all values in the specified submatrix by 1.

This solution uses a 2D difference array technique to efficiently handle multiple 
range updates in O(1) time per query, then reconstructs the final matrix using 
2D prefix sums.

Approach:
1. Use a 2D difference array to mark the boundaries of each increment operation
2. Apply 2D prefix sums to compute the final values

Time Complexity: O(n² + q) where q is the number of queries
Space Complexity: O(n²) for the difference array and result matrix

URL: https://leetcode.com/problems/increment-submatrices-by-one/
"""
from typing import List

import pytest


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """
        Apply range increment queries to an n x n matrix and return the final state.
        
        Args:
            n (int): Size of the square matrix
            queries (List[List[int]]): List of queries, each with [row1, col1, row2, col2]
                                     representing the submatrix corners
            
        Returns:
            List[List[int]]: Final state of the matrix after applying all queries
            
        Example:
            >>> s = Solution()
            >>> s.rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]])
            [[1, 1, 0], [1, 2, 1], [0, 1, 1]]
        """
        # Initialize 2D difference array with padding to avoid boundary checks
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        # Process each query using 2D difference technique
        # For a rectangle from (r1,c1) to (r2,c2):
        # - Add 1 at (r1, c1) - top-left corner
        # - Subtract 1 at (r1, c2+1) - just right of top-right corner
        # - Subtract 1 at (r2+1, c1) - just below bottom-left corner
        # - Add 1 at (r2+1, c2+1) - just below and right of bottom-right corner
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # Initialize result matrix
        matrix = [[0] * n for _ in range(n)]

        # Reconstruct the final matrix using 2D prefix sums
        # For each cell, calculate the cumulative effect of all difference operations
        for i in range(n):
            for j in range(n):
                # Compute 2D prefix sum at position (i,j)
                # Add contribution from the cell above
                if i > 0:
                    diff[i][j] += diff[i - 1][j]
                # Add contribution from the cell to the left
                if j > 0:
                    diff[i][j] += diff[i][j - 1]
                # Subtract overcounted contribution from the diagonal cell
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i - 1][j - 1]
                # Assign computed value to result matrix
                matrix[i][j] = diff[i][j]

        return matrix


@pytest.mark.parametrize("n, queries, expected", [
        # Example 1 from problem statement
        (3, [[1, 1, 2, 2], [0, 0, 1, 1]],
         [[1, 1, 0],
          [1, 2, 1],
          [0, 1, 1]]),

        # Example 2 from problem statement
        (2, [[0, 0, 1, 1]],
         [[1, 1],
          [1, 1]]),

        # Single point queries
        (4, [[0, 0, 0, 0], [3, 3, 3, 3]],
         [[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]]),

        # Full matrix query
        (3, [[0, 0, 2, 2]],
         [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]),

        # No queries
        (3, [],
         [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]),

        # Multiple overlapping queries
        (2, [[0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]],
         [[3, 3],
          [3, 3]]),
    ]
)
def test_solutions(n, queries, expected):
    sol = Solution()
    assert sol.rangeAddQueries(n, queries) == expected