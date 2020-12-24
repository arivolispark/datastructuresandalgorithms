
"""
Title:  Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true



Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false



Example 3:

Input: root = []
Output: true
 

Constraints:

1) The number of nodes in the tree is in the range [0, 5000].
2) -10^4 <= Node.val <= 10^4

"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return is_balanced_helper(root) > -1
        
        
def is_balanced_helper(root):
    if root is None:
        return 0

    left_height = is_balanced_helper(root.left)

    if left_height == -1:
        return -1

    right_height = is_balanced_helper(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1        


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()
