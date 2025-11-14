"""
LeetCode 0001 – Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target. You may assume that each input would have exactly one 
solution, and you may not use the same element twice.

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(n) - Hash map to store elements and their indices

URL: https://leetcode.com/problems/two-sum/
"""
from typing import List

import pytest

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that sum to the target value.
        
        Args:
            nums (List[int]): Array of integers
            target (int): Target sum value
            
        Returns:
            List[int]: Indices of the two numbers that sum to target
            
        Example:
            >>> s = Solution()
            >>> s.twoSum([2,7,11,15], 9)
            [0, 1]
        """
        # Dictionary to store number -> index mapping for O(1) lookup
        num_to_index = {}
        
        # Iterate through the array with index
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num
            
            # If complement exists in our map, we found the solution
            if complement in num_to_index:
                # Return [index of complement, current index]
                return [num_to_index[complement], i]
            
            # Store current number and its index for future lookups
            num_to_index[num] = i
            
        # This line should never be reached given problem constraints
        # (exactly one solution exists)
        return []


@pytest.mark.parametrize("nums, target, expected", [
    ([2,7,11,15], 9, [0, 1]),
    ([3,2,4], 6, [1, 2]),
    ([3,3], 6, [0, 1]),
])
def test_solutions(nums, target, expected):
    sol = Solution()
    assert sol.twoSum(nums, target) == expected