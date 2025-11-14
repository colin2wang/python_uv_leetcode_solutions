"""
LeetCode 0010 – Regular Expression Matching

Implement regular expression matching with support for '.' and '*':
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

This solution uses dynamic programming to solve the problem:
1. Create a 2D DP table where dp[i][j] represents whether s[0:i] matches p[0:j]
2. Handle base cases for empty string and pattern
3. Process the pattern character by character, handling special cases for '*'
4. Fill the DP table based on matching rules

Time Complexity: O(m*n) where m is length of string and n is length of pattern
Space Complexity: O(m*n) for the DP table

Examples:
- isMatch("aa", "a") → False
- isMatch("aa", "a*") → True
- isMatch("ab", ".*") → True

URL: https://leetcode.com/problems/regular-expression-matching/
"""
import pytest

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Determine if input string matches the given pattern.
        
        Args:
            s (str): Input string to match
            p (str): Pattern string with support for '.' and '*'
            
        Returns:
            bool: True if s matches pattern p completely, False otherwise
            
        Examples:
            >>> sol = Solution()
            >>> sol.isMatch("aa", "a")
            False
            >>> sol.isMatch("aa", "a*")
            True
            >>> sol.isMatch("ab", ".*")
            True
        """
        # Quick optimizations for common cases
        if p == '.*':
            return True
        if s == p:
            return True

        # Get lengths of string and pattern
        m, n = len(s), len(p)
        
        # Initialize DP table: dp[i][j] represents whether s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns that can match empty string (patterns with '*')
        # These are patterns like a*, a*b*, etc. where '*' means "zero occurrences"
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' can represent zero occurrences of the preceding character
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table for all combinations of string and pattern prefixes
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case 1: Current pattern char is not '*'
                if p[j - 1] != '*':
                    # Match occurs if:
                    # 1. Characters are identical, OR
                    # 2. Pattern has '.', which matches any character
                    # AND the previous substrings also matched
                    if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                # Case 2: Current pattern char is '*'
                else:
                    # '*' represents zero occurrences of the preceding character
                    dp[i][j] = dp[i][j - 2]
                    
                    # '*' represents one or more occurrences if:
                    # 1. The preceding character matches current string character, OR
                    # 2. The preceding character is '.' (matches any character)
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        # Either zero occurrences OR extend previous match
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        # Return whether the entire string matches the entire pattern
        return dp[m][n]


@pytest.mark.parametrize("s, p, expected", [
    ("aa", "a", False),     # Pattern 'a' doesn't match string 'aa'
    ("aa", "a*", True),     # '*' matches zero or more 'a', so 'a*' matches 'aa'
    ("ab", ".*", True),     # '.*' matches any string
    ("aab", "c*a*b", True), # 'c*' matches zero 'c', then 'a*' matches 'aa', then 'b' matches 'b'
])
def test_solutions(s, p, expected):
    """Test the regular expression matching implementation with various cases."""
    sol = Solution()
    assert sol.isMatch(s, p) == expected