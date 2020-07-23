"""
Title:  Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of
its nodes' values. (ie, from left to right, then right to left
for the next level and alternate between).


For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7


return its zigzag level order traversal as:


[
  [3],
  [20,9],
  [15,7]
]

"""

from typing import List
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        left_to_right = True

        if root:
            q = deque()
            q.append(root)
            while q:
                level_list = list()
                for i in range(len(q)):
                    node = q.popleft()
                    if node:
                        if left_to_right:
                            level_list.append(node.val)
                        else:
                            level_list.insert(0, node.val)

                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                left_to_right = not left_to_right
                result.append(level_list)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1() -> TreeNode:
    """
    3
   / \
  9  20
    /  \
   15   7

    """

    node_1 = TreeNode(3)
    node_2 = TreeNode(9)
    node_3 = TreeNode(20)
    node_4 = TreeNode(15)
    node_5 = TreeNode(7)

    node_1.left = node_2
    node_1.right = node_3
    node_3.left = node_4
    node_3.right = node_5

    head = node_1

    return head


if __name__ == "__main__":
    solution = Solution()

    test(solution.zigzagLevelOrder(get_test_case_1()), [[3],[20,9],[15,7]])
