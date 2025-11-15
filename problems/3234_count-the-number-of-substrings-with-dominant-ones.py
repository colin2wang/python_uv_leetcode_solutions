"""
LeetCode 3234 – Count The Number Of Substrings With Dominant Ones

URL: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/
"""
import pytest


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Count substrings where (number of 0s)² ≤ (number of 1s).
        
        Algorithm Explanation:
        1. Preprocessing Phase:
           - Build a 'pre' array where pre[i] stores the index of the nearest '0' 
             to the left of position i (or -1 if none exists)
           - This helps us efficiently navigate through segments of consecutive characters
        
        2. Main Computation:
           - For each position i, we look at all possible substrings ending at i
           - We iterate backwards through segments of consecutive '0's
           - For each segment, we calculate the count of 0s and 1s
           - We check if count0² ≤ count1 (the dominance condition)
           - If satisfied, we count how many valid substrings we can form
        
        Time Complexity: O(n * √n) where n is the length of the string
        Space Complexity: O(n) for the preprocessing array
        
        Args:
            s (str): Binary string containing only '0' and '1' characters
            
        Returns:
            int: Number of substrings with dominant ones
        """
        n = len(s)
        
        # Preprocessing: Build array to track nearest zero to the left
        # pre[i] = index of nearest '0' to the left of position i, or -1 if none exists
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == '0':
                # Either at the beginning or found a '0' at previous position
                pre[i + 1] = i
            else:
                # Continue the chain from the previous position
                pre[i + 1] = pre[i]

        res = 0
        
        # For each position i (1-indexed) in the string
        for i in range(1, n + 1):
            # Count of zeros ending exactly at position i-1 (0-indexed)
            cnt0 = 1 if s[i - 1] == '0' else 0
            j = i  # Position pointer for backward traversal
            
            # Optimization: Stop when cnt0² exceeds string length
            # Since we need cnt0² ≤ cnt1, and cnt1 ≤ n, we can prune early
            while j > 0 and cnt0 * cnt0 <= n:
                # Calculate count of ones in substring from pre[j] to i-1
                # Total length: (i - pre[j]), subtract zeros: cnt0
                cnt1 = (i - pre[j]) - cnt0
                
                # Check dominance condition: (zeros)² ≤ (ones)
                if cnt0 * cnt0 <= cnt1:
                    # Count valid substrings in this segment
                    # Take minimum of:
                    # 1. Length of current zero-segment: (j - pre[j])
                    # 2. How many extra ones we have beyond the required threshold: (cnt1 - cnt0² + 1)
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                
                # Move to the previous segment of zeros
                j = pre[j]
                cnt0 += 1  # Increment zero count as we move to the next segment
                
        return res


@pytest.mark.parametrize("s, expected", [
    ("00011", 5),
    ("101101", 16),
    ("111", 6),
    ("0", 0),           # Single '0': 1² = 1 > 0 ones → Not dominant
    ("1", 1),           # Single '1': 0² = 0 ≤ 1 ones → Dominant
    ("01", 2),          # Valid substrings: "01" (0²≤1) and "1"
    ("10", 2),          # Valid substrings: "10" (0²≤1) and "1"
    ("0011", 5),        # Multiple valid substrings
    ("1100", 5),        # Fewer valid substrings
    ("101", 5),         # Mixed pattern
    ("0101", 6),        # Alternating pattern
    ("1111", 10),       # All substrings valid (no zeros)
    ("0000", 0),        # No valid substrings (only zeros)
    ("10101", 9),       # Complex mixed pattern
    ("00111", 9),       # Test case with clear dominance
])
def test_solutions(s, expected):
    """
    Comprehensive test suite for the numberOfSubstrings function.
    
    Test Cases Cover:
    - Original examples from the problem statement
    - Edge cases with single characters
    - Strings with only 0s or only 1s
    - Various patterns of 0s and 1s
    - Cases that clearly satisfy or violate the dominance condition
    
    Args:
        s (str): Input binary string
        expected (int): Expected number of substrings with dominant ones
    """
    sol = Solution()
    assert sol.numberOfSubstrings(s) == expected