"""
LeetCode 0021 – Merge Two Sorted Lists

URL: https://leetcode.com/problems/merge-two-sorted-lists/
"""
from typing import Optional

import pytest

# Definition for singly-linked list.
class ListNode:
    """
    A node in a singly-linked list.
    
    Attributes:
        val (int): The value stored in the node
        next (Optional[ListNode]): Reference to the next node in the list
    """
    def __init__(self, val=0, next=None):
        """
        Initialize a ListNode with a value and optional next node reference.
        
        Args:
            val (int): The value to store in the node. Defaults to 0.
            next (Optional[ListNode]): Reference to the next node. Defaults to None.
        """
        self.val = val
        self.next = next

# Build ListNodes from lists
def build_list_node(lst: list) -> Optional[ListNode]:
    """
    Convert a Python list to a linked list of ListNodes.
    
    Args:
        lst (list): A list of values to convert to a linked list
        
    Returns:
        Optional[ListNode]: The head of the created linked list, or None if the input list is empty
    """
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Convert ListNodes to lists
def list_node_to_list(listNode: Optional[ListNode]) -> list:
    """
    Convert a linked list of ListNodes to a Python list.
    
    Args:
        listNode (Optional[ListNode]): The head of the linked list to convert
        
    Returns:
        list: A Python list containing all values from the linked list in order
    """
    if not listNode:
        return []
    list = []
    while listNode:
        list.append(listNode.val)
        listNode = listNode.next
    return list

def compare_list_node(listNode1: Optional[ListNode], listNode2: Optional[ListNode]) -> bool:
    """
    Compare two linked lists for equality by checking each node's value.
    
    Args:
        listNode1 (Optional[ListNode]): Head of the first linked list
        listNode2 (Optional[ListNode]): Head of the second linked list
        
    Returns:
        bool: True if both lists have the same values in the same order, False otherwise
    """
    while listNode1 and listNode2:
        if listNode1.val != listNode2.val:
            return False
        listNode1 = listNode1.next
        listNode2 = listNode2.next
    return listNode1 is None and listNode2 is None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list.
        
        This function takes two sorted linked lists and merges them into a single
        sorted linked list by splicing together the nodes of the first two lists.
        
        Approach:
        - Use a dummy head node to simplify the merging process
        - Compare nodes from both lists and attach the smaller one to the result
        - Continue until one list is exhausted, then append the remaining nodes
        
        Time Complexity: O(m + n) where m and n are the lengths of the two lists
        Space Complexity: O(1) as we only use a constant amount of extra space
        
        Args:
            list1 (Optional[ListNode]): Head of the first sorted linked list
            list2 (Optional[ListNode]): Head of the second sorted linked list
            
        Returns:
            Optional[ListNode]: Head of the merged sorted linked list
            
        Examples:
            >>> # Merging [1,2,4] and [1,3,4] results in [1,1,2,3,4,4]
            >>> # Merging [] and [] results in []
            >>> # Merging [] and [0] results in [0]
        """
        # Create a dummy head node to simplify edge cases and maintain reference to the start
        dummy = ListNode(-1)
        # Current pointer to track the end of our merged list
        cur = dummy

        # Traverse both lists while both have nodes remaining
        while list1 and list2:
            # Compare values and attach the smaller node to our merged list
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            # Move our current pointer forward
            cur = cur.next

        # Attach remaining nodes from whichever list still has nodes
        # Since the lists are already sorted, we can directly attach the remainder
        cur.next = list1 if list1 else list2
        # Return the head of the merged list (skip the dummy node)
        return dummy.next


@pytest.mark.parametrize("list1, list2, expected", [
    (build_list_node([1,2,4]), build_list_node([1,3,4]), build_list_node([1,1,2,3,4,4])),
    (build_list_node([]), build_list_node([]), build_list_node([])),
    (build_list_node([]), build_list_node([0]), build_list_node([0])),
])
def test_solutions(list1: Optional[ListNode], list2: Optional[ListNode], expected: Optional[ListNode]):
    sol = Solution()
    assert compare_list_node(sol.mergeTwoLists(list1, list2), expected) is True