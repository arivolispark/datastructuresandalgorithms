"""
Title:  Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in
the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest
to the target.


Example:
Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

"""

import math
from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def closestValue(self, root: TreeNode, target: float) -> int:
        closest_diff = math.inf
        result = 0
        inorder_list = []
        inorder_traversal(root, inorder_list)
        #print(" inorder_list: ", inorder_list)

        if inorder_list:
            result = inorder_list[0]
            start, end = 0, len(inorder_list) - 1
            while start <= end:
                mid = start + (end - start) // 2
                diff = abs(inorder_list[mid] - target)
                if diff < closest_diff:
                    closest_diff = diff
                    result = inorder_list[mid]

                if inorder_list[mid] == target:
                    return inorder_list[mid]
                elif inorder_list[mid] < target:
                    start = mid + 1
                elif inorder_list[mid] > target:
                    end = mid - 1
        return result


def inorder_traversal(root: TreeNode, inorder_list: List[int]) -> int:
    if root is None:
        return
    inorder_traversal(root.left, inorder_list)
    inorder_list.append(root.val)
    inorder_traversal(root.right, inorder_list)


def get_test_case_1_input() -> TreeNode:
    """
    4
   / \
  2   5
 / \
1   3

    """

    node_1 = TreeNode(4)
    node_2 = TreeNode(2)
    node_3 = TreeNode(5)
    node_4 = TreeNode(1)
    node_5 = TreeNode(3)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    return node_1


def get_test_case_2_input() -> TreeNode:
    """
    1

    """

    node_1 = TreeNode(1)

    return node_1


def get_test_case_3_input() -> TreeNode:
    """
        2
      /
    1

    """

    node_1 = TreeNode(2)
    node_2 = TreeNode(1)

    node_1.left = node_2

    return node_1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        get_test_case_1_input(),
        get_test_case_2_input(),
        get_test_case_3_input()
    ]

    test_case_targets = [
        3.714286,
        4.428571,
        2147483647.0
    ]

    test_case_outputs = [
        4,
        1,
        2
    ]

    for i in range(len(test_case_inputs)):
        test(solution.closestValue(test_case_inputs[i], test_case_targets[i]), test_case_outputs[i])
