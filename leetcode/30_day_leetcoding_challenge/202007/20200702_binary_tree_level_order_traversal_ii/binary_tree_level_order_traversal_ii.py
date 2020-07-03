"""
Title:  Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of
its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:


[
  [15,7],
  [9,20],
  [3]
]


"""

from typing import List
from collections import *


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        q = deque()

        if root:
            q.append(root)

            while q:
                level_list = list()

                for i in range(len(q)):
                    node = q.popleft()
                    level_list.append(node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

                if level_list:
                    result.insert(0, level_list)
        return result


def get_test_case_1() -> TreeNode:
    """

Given binary tree [3,9,20,null,null,15,7],


    3
   / \
  9  20
    /  \
   15   7

    :return:
    """

    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)

    three.left = nine
    three.right = twenty

    twenty.left = fifteen
    twenty.right = seven

    head = three

    return head


def get_test_case_2() -> TreeNode:
    """

Given binary tree [3,9,20,null,null,15,7],

       1
      / \
     2   3
    /     \
   4       5

    :return:
    """

    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    one.left = two
    one.right = three

    two.left = four
    three.right = five

    head = one

    return head


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        get_test_case_1(),
        get_test_case_2()
    ]

    test_case_outputs = [
        [[15, 7], [9, 20], [3]],
        [[4, 5], [2, 3], [1]]
    ]

    for i in range(len(test_case_inputs)):
        test(solution.levelOrderBottom(test_case_inputs[i]), test_case_outputs[i])
