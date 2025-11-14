"""
LeetCode 0061 – Rotate List

URL: https://leetcode.com/problems/rotate-list/
"""

from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_node_to_list(node: ListNode) -> Optional[list]:
    """
    Convert a linked list to a Python list for easy comparison.
    
    Args:
        node: The head node of the linked list
        
    Returns:
        A Python list containing all values from the linked list, or None if the list is empty
    """
    if node is None:
        return None

    result = []
    while node:
        result.append(node.val)
        node = node.next

    return result

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate the linked list to the right by k places.
        
        Args:
            head: The head node of the linked list
            k: Number of positions to rotate right
            
        Returns:
            The new head node after rotation
        """
        if head is None:
            return None

        # Calculate list length and find tail node
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # If k is a multiple of length, no rotation needed
        k = k % length
        if k == 0:
            return head

        # Connect tail to head to form circular list
        tail.next = head

        # Find new tail: (length-k)th node from head
        new_tail = head
        for i in range(length - k - 1):
            new_tail = new_tail.next

        # New head is the next node of new tail
        new_head = new_tail.next
        
        # Break the circle to form new list
        new_tail.next = None

        return new_head


@pytest.mark.parametrize("head, k, expected", [
    (ListNode(1, ListNode(2)), 1, ListNode(2, ListNode(1))),
    (None, 0, None),
    (ListNode(0, ListNode(1, ListNode(2))), 4, ListNode(2, ListNode(0, ListNode(1)))),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))),
])
def test_solutions(head, k, expected):
    sol = Solution()
    assert list_node_to_list(sol.rotateRight(head, k)) == list_node_to_list(expected)