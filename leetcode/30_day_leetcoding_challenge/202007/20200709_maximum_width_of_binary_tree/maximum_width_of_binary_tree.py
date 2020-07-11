"""
Title:  Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the
given tree. The width of a tree is the maximum width among all levels.
The binary tree has the same structure as a full binary tree, but some
nodes are null.

The width of one level is defined as the length between the end-nodes (the
leftmost and right most non-null nodes in the level, where the null nodes
between the end-nodes are also counted into the length calculation.

Example 1:
Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).



Example 2:
Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).


Example 3:
Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).


Example 4:
Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.


"""

from typing import List
from collections import *


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 1
        q = [[root, 0]]

        while q:
            count = len(q)
            start = q[0][1]
            end = q[-1][1]
            max_width = max(end - start + 1, max_width)

            for i in range(count):
                p = q[0]
                index = p[1] - start
                q.pop(0)

                if p[0].left is not None:
                    q.append([p[0].left, 2 * index + 1])

                if p[0].right is not None:
                    q.append([p[0].right, 2 * index + 2])
        return max_width


def get_test_case_1():
    return None


def get_test_case_2():
    return TreeNode(1)


def get_test_case_3():
    """
           1
         /   \
        3     2
    """
    node_1 = TreeNode(1)
    node_2 = TreeNode(3)
    node_3 = TreeNode(2)

    node_1.left = node_2
    node_1.right = node_3

    return node_1


def get_test_case_4():
    """
           1
         /   \
        3     2
       / \     \
      5   3     9

    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(3)
    node_3 = TreeNode(2)
    node_4 = TreeNode(5)
    node_5 = TreeNode(3)
    node_6 = TreeNode(9)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.right = node_6

    return node_1


def get_test_case_5():
    """
          1
         /
        3
       / \
      5   3

    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(3)
    node_3 = TreeNode(5)
    node_4 = TreeNode(3)

    node_1.left = node_2
    node_2.left = node_3
    node_2.right = node_4

    return node_1


def get_test_case_6():
    """
          1
         / \
        3   2
       /
      5

    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(3)
    node_3 = TreeNode(2)
    node_4 = TreeNode(5)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4

    return node_1


def get_test_case_7():
    """

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7

    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(3)
    node_3 = TreeNode(2)
    node_4 = TreeNode(5)
    node_5 = TreeNode(9)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_4.left = node_6

    node_3.right = node_5
    node_5.right = node_7

    return node_1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.widthOfBinaryTree(get_test_case_1()), 0)
    test(solution.widthOfBinaryTree(get_test_case_2()), 1)
    test(solution.widthOfBinaryTree(get_test_case_3()), 2)
    test(solution.widthOfBinaryTree(get_test_case_4()), 4)
    test(solution.widthOfBinaryTree(get_test_case_5()), 2)
    test(solution.widthOfBinaryTree(get_test_case_6()), 2)
    test(solution.widthOfBinaryTree(get_test_case_7()), 8)
