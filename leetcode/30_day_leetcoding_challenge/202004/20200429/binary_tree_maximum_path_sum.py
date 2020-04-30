"""
Title:  Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes
from some starting node to any node in the tree along the
parent-child connections. The path must contain at least
one node and does not need to go through the root.


Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6


Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


import math


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = -math.inf

        def dfs(root: TreeNode) -> int:
            if root is None:
                return 0

            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))
            self.maximum = max(left_max + right_max + root.val, self.maximum)
            return max(left_max, right_max) + root.val

        dfs(root)
        return self.maximum


def inorder_traversal(root: TreeNode):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)


def get_test_case_1() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)

    one.left = two
    one.right = three

    return one


def get_test_case_2() -> TreeNode:
    minus_ten = TreeNode(-10)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)

    minus_ten.left = nine
    minus_ten.right = twenty
    twenty.left = fifteen
    twenty.right = seven

    return minus_ten


def get_test_case_3() -> TreeNode:
    """
    Example:
    Input: [2, -1]

       2
      /
     /
   -1


    Output: 2
    """

    node_1 = TreeNode(2)
    node_2 = TreeNode(-1)

    node_1.left = node_2

    return node_1


def get_test_case_4() -> TreeNode:
    node_1 = TreeNode(-3)

    return node_1


def get_test_case_5() -> TreeNode:
    """
    Example:
    Input: [1, -2, 3]

       1
      / \
     /   \
   -2     3


    Output: 4
    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(-2)
    node_3 = TreeNode(3)

    node_1.left = node_2
    node_1.right = node_3

    return node_1


def get_test_case_6() -> TreeNode:
    return None


def get_test_case_7() -> TreeNode:
    return None


if __name__ == "__main__":
    solution = Solution()

    #root = get_test_case_1()
    root = get_test_case_2()
    #root = get_test_case_3()
    #root = get_test_case_4()
    #root = get_test_case_5()
    inorder_traversal(root)

    max_path_sum = solution.maxPathSum(root)
    print("\n max_path_sum: ", max_path_sum)
