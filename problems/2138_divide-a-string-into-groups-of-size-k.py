"""
LeetCode 2138 – Divide A String Into Groups Of Size K

Given a string s, divide it into groups of size k. For the last group, if it has less 
than k characters, fill the remaining positions with the fill character.

Approach:
1. Iterate through the string in steps of k
2. Extract substrings of length k
3. For the last group, if its length is less than k, pad it with the fill character

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for the result list

URL: https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
"""
from typing import List

import pytest


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        """
        Divide a string into groups of size k, padding the last group if necessary.
        
        Args:
            s (str): Input string to be divided
            k (int): Size of each group
            fill (str): Character to use for padding the last group if needed
            
        Returns:
            List[str]: List of strings where each string has length k
            
        Example:
            >>> s = Solution()
            >>> s.divideString("abcdefghi", 3, "x")
            ["abc", "def", "ghi"]
            >>> s.divideString("abcdefghij", 3, "x")
            ["abc", "def", "ghi", "jxx"]
        """
        # Initialize result list to store groups
        res = []
        
        # Iterate through the string in steps of k
        for i in range(0, len(s), k):
            # Extract substring of length k starting at index i
            res.append(s[i:i + k])
        
        # Check if the last group needs padding
        if len(res[-1]) < k:
            # Pad the last group with fill characters to make its length equal to k
            res[-1] += fill * (k - len(res[-1]))
            
        # Return the list of groups
        return res


@pytest.mark.parametrize("s, k, fill, expected", [
    ("abcdefghi", 3, "x", ["abc", "def", "ghi"]),
    ("abcdefghij", 3, "x", ["abc", "def", "ghi", "jxx"]),
])
def test_solutions(s, k, fill, expected):
    sol = Solution()
    assert sol.divideString(s, k, fill) == expected