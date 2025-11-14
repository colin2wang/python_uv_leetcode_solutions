"""
LeetCode 0028 – Find The Index Of The First Occurrence In A String

URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""
import pytest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


@pytest.mark.parametrize("haystack, needle, expected", [
    ("hello", "ll", 2),
    ("aaaaa", "bba", -1),
    ("mississippi", "issip", 4),
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
    ("", "", 0),
])
def test_solutions(haystack, needle, expected):
    sol = Solution()
    assert sol.strStr(haystack, needle) == expected
