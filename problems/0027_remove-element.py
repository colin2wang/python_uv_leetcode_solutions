"""
LeetCode 0027 – Remove Element

URL: https://leetcode.com/problems/remove-element/
"""
from operator import length_hint
from typing import List

import pytest


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        strat, end = 0, length - 1
        while strat <= end:
            while strat < length and nums[strat] != val:
                strat += 1
            while nums[end] == val and end >= 0:
                end -= 1
            if strat < end:
                nums[strat], nums[end] = nums[end], nums[strat]

        return strat


@pytest.mark.parametrize("nums, val, expected_len, expected_nums", [
    ([4, 5], 5, 1, [4]),
    ([1], 1, 0, []),
    ([3, 2, 2, 3], 3, 2, [2, 2]),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
])
def test_solutions(nums, val, expected_len, expected_nums):
    sol = Solution()
    actual_len = sol.removeElement(nums, val)
    assert actual_len == expected_len
    assert sorted(nums[0:actual_len]) == sorted(expected_nums)
