"""
LeetCode 0110 – Balanced Binary Tree

URL: https://leetcode.com/problems/balanced-binary-tree/
"""
from typing import Optional

import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if a binary tree is height-balanced.
        
        A height-balanced binary tree is defined as a binary tree in which the 
        depth of the two subtrees of every node never differs by more than one.
        
        Approach:
        - Use a helper function that returns the height of the tree
        - If subtree is unbalanced, return -1 as indicator
        - Otherwise return actual height
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        
        Args:
            root (Optional[TreeNode]): Root of the binary tree
            
        Returns:
            bool: True if the tree is balanced, False otherwise
        """
        def check_height(node: Optional[TreeNode]) -> int:
            """
            Helper function to compute height and check balance.
            
            Returns:
                int: Height of the tree if balanced, -1 if unbalanced
            """
            # Base case: empty node has height 0
            if not node:
                return 0
            
            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:  # Left subtree is unbalanced
                return -1
            
            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:  # Right subtree is unbalanced
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1  # Current node is unbalanced
            
            # Return height of current node
            return max(left_height, right_height) + 1
        
        # Tree is balanced if check_height doesn't return -1
        return check_height(root) != -1


@pytest.mark.parametrize("root, expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), True),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)), False),
    (None, True),
])
def test_solutions(root, expected):
    sol = Solution()
    assert sol.isBalanced(root) == expected