"""
LeetCode 0005 – Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.
A palindrome is a string that reads the same forwards and backwards.

Approach:
- Use the "expand around centers" technique
- For each possible center position, expand outward while characters match
- Handle both odd-length palindromes (single character center) and 
  even-length palindromes (between two characters)
  
Time Complexity: O(n²) - where n is the length of the string
Space Complexity: O(1) - only using a constant amount of extra space

URL: https://leetcode.com/problems/longest-palindromic-substring/
"""
import pytest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in the given string.
        
        Args:
            s (str): Input string
            
        Returns:
            str: Longest palindromic substring
            
        Example:
            >>> s = Solution()
            >>> s.longestPalindrome("babad")
            "bab"  # "aba" is also valid
            >>> s.longestPalindrome("cbbd")
            "bb"
        """
        # Handle edge case of empty string
        if not s:
            return ""
            
        # Get length of string and initialize tracking variables
        n = len(s)
        start, max_len = 0, 1  # Start index and length of longest palindrome found

        def expand(l: int, r: int):
            """
            Expand around center positions l and r while characters match.
            
            Args:
                l (int): Left pointer index
                r (int): Right pointer index
            """
            nonlocal start, max_len
            
            # Expand outward while characters match and indices are valid
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1  # Move left pointer leftward
                r += 1  # Move right pointer rightward

            # Calculate length of palindrome found
            # r - l - 1 because l and r are now pointing outside the palindrome
            cur_len = r - l - 1
            
            # Update global maximum if current palindrome is longer
            if cur_len > max_len:
                # l + 1 because l is now pointing to position before palindrome start
                start, max_len = l + 1, cur_len

        # Check all possible centers
        for i in range(n):
            # Check for odd-length palindromes (center at i)
            expand(i, i)
            
            # Check for even-length palindromes (center between i and i+1)
            expand(i, i + 1)

        # Return the longest palindromic substring
        return s[start: start + max_len]


@pytest.mark.parametrize("s, expected", [
    ("babad", "bab"),
    ("cbbd", "bb"),
])
def test_solutions(s, expected):
    sol = Solution()
    assert sol.longestPalindrome(s) == expected