
"""
Title:  Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:

               3
              /  \
            9    20
                /  \
               15   7

Input: root = [3,9,20,null,null,15,7]
Output: 3



Example 2:

               1
                \
                 2

Input: root = [1,null,2]
Output: 2



Example 3:
Input: root = []
Output: 0



Example 4:

               0

Input: root = [0]
Output: 1


Constraints:

1) The number of nodes in the tree is in the range [0, 10^4].
2) -100 <= Node.val <= 100

"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def test_case_1_input():
    node_1 = TreeNode(3)
    node_2 = TreeNode(9)
    node_3 = TreeNode(20)
    node_4 = TreeNode(15)
    node_5 = TreeNode(7)

    node_1.left = node_2
    node_1.right = node_3

    node_3.left = node_4
    node_3.right = node_5

    return node_1


def test_case_2_input():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)

    node_1.right = node_2

    return node_1


def test_case_3_input():
    return None


def test_case_4_input():
    node_1 = TreeNode(0)

    return node_1


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxDepth(test_case_1_input()), 3)
    test(solution.maxDepth(test_case_2_input()), 2)
    test(solution.maxDepth(test_case_3_input()), 0)
    test(solution.maxDepth(test_case_4_input()), 1)

