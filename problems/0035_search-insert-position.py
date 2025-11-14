"""
LeetCode 0035 – Search Insert Position

URL: https://leetcode.com/problems/search-insert-position/
"""
from typing import List

import pytest


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


@pytest.mark.parametrize("nums, target, expected", [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
])
def test_solutions(nums, target, expected):
    sol = Solution()
    assert sol.searchInsert(nums, target) == expected