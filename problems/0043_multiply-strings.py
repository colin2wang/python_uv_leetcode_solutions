"""
LeetCode 0043 – Multiply Strings

URL: https://leetcode.com/problems/multiply-strings/
"""
import pytest


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


@pytest.mark.parametrize("num1, num2, expected", [
    ("2", "3", "6"),
    ("123", "456", "56088"),
])
def test_solutions(num1, num2, expected):
    sol = Solution()
    assert sol.multiply(num1, num2) == expected
