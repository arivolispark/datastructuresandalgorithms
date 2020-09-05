"""
Title:  All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.



Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]



Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]



Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]



Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]



Example 5:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]


Constraints:
1) Each tree has at most 5000 nodes.
2) Each node's value is between [-10^5, 10^5].

"""


from typing import List
from heapq import *


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        min_heap = []
        result = []

        if root1:
            inorder_traversal(root1, min_heap)
        if root2:
            inorder_traversal(root2, min_heap)

        while min_heap:
            result.append(heappop(min_heap))
        return result


def inorder_traversal(root: TreeNode, min_heap: List[int]):
    if root is None:
        return
    heappush(min_heap, root.val)
    inorder_traversal(root.left, min_heap)
    inorder_traversal(root.right, min_heap)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_tree_1_input() -> TreeNode:
    """
          2
        /  \
       1   4

    :return:
    """

    node_1 = TreeNode(2)
    node_2 = TreeNode(1)
    node_3 = TreeNode(4)

    node_1.left = node_2
    node_1.right = node_3

    root = node_1

    return root


def get_test_case_1_tree_2_input() -> TreeNode:
    """
          1
        /  \
       0   3

    :return:
    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(0)
    node_3 = TreeNode(3)

    node_1.left = node_2
    node_1.right = node_3

    root = node_1

    return root


def get_test_case_1_output() -> List[int]:
    return [0,1,1,2,3,4]


def get_test_case_2_tree_1_input() -> TreeNode:
    """
          0
        /  \
     -10   10

    :return:
    """

    node_1 = TreeNode(0)
    node_2 = TreeNode(-10)
    node_3 = TreeNode(10)

    node_1.left = node_2
    node_1.right = node_3

    root = node_1

    return root


def get_test_case_2_tree_2_input() -> TreeNode:
    """
          5
        /  \
       1   7
      / \
     0   2

    :return:
    """

    node_1 = TreeNode(5)
    node_2 = TreeNode(1)
    node_3 = TreeNode(7)
    node_4 = TreeNode(0)
    node_5 = TreeNode(2)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5

    root = node_1

    return root


def get_test_case_2_output() -> List[int]:
    return [-10,0,0,1,2,5,7,10]


def get_test_case_3_tree_1_input() -> TreeNode:
    """
       None

    :return:
    """

    return None


def get_test_case_3_tree_2_input() -> TreeNode:
    """
          5
        /  \
       1   7
      / \
     0   2

    :return:
    """

    node_1 = TreeNode(5)
    node_2 = TreeNode(1)
    node_3 = TreeNode(7)
    node_4 = TreeNode(0)
    node_5 = TreeNode(2)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5

    root = node_1

    return root


def get_test_case_3_output() -> List[int]:
    return [0,1,2,5,7]


def get_test_case_4_tree_1_input() -> TreeNode:
    """
          0
        /  \
     -10   10

    :return:
    """

    node_1 = TreeNode(0)
    node_2 = TreeNode(-10)
    node_3 = TreeNode(10)

    node_1.left = node_2
    node_1.right = node_3

    root = node_1

    return root


def get_test_case_4_tree_2_input() -> TreeNode:
    """
          None

    :return:
    """

    return None


def get_test_case_4_output() -> List[int]:
    return [-10,0,10]


def get_test_case_5_tree_1_input() -> TreeNode:
    """
          1
           \
           8

    :return:
    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(8)

    node_1.right = node_2

    root = node_1

    return root


def get_test_case_5_tree_2_input() -> TreeNode:
    """
          8
         /
        1

    :return:
    """

    node_1 = TreeNode(8)
    node_2 = TreeNode(1)

    node_1.left = node_2

    root = node_1

    return root


def get_test_case_5_output() -> List[int]:
    return [1,1,8,8]


if __name__ == "__main__":
    solution = Solution()

    test(solution.getAllElements(get_test_case_1_tree_1_input(), get_test_case_1_tree_2_input()), get_test_case_1_output())
    test(solution.getAllElements(get_test_case_2_tree_1_input(), get_test_case_2_tree_2_input()), get_test_case_2_output())
    test(solution.getAllElements(get_test_case_3_tree_1_input(), get_test_case_3_tree_2_input()), get_test_case_3_output())
    test(solution.getAllElements(get_test_case_4_tree_1_input(), get_test_case_4_tree_2_input()), get_test_case_4_output())
    test(solution.getAllElements(get_test_case_5_tree_1_input(), get_test_case_5_tree_2_input()), get_test_case_5_output())
