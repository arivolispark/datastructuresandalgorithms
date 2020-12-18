
"""
Title:  Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 


Example 1:
Input: root = [2,1,3]
Output: true



Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 


Constraints:

1) The number of nodes in the tree is in the range [1, 104].
2) -2^31 <= Node.val <= 2^31 - 1


"""

from typing import List


class TreeNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if (not node):
                return True

            if (node.val<=lower or node.val>=upper):
                return False
            if not helper(node.right, node.val, upper):
                return False
            if not helper(node.left, lower, node.val):
                return False
            return True


        return helper(root)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()
