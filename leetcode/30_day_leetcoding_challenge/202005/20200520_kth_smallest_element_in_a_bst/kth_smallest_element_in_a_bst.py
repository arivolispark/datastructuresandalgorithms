"""
Title:  Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest
to find the kth smallest element in it.


Example 1:
Input: root = [3,1,4,null,2], k = 1

   3
  / \
 1   4
  \
   2

Output: 1


Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3

       5
      / \
     3   6
    / \
   2   4
  /
 1

Output: 3


Follow up:
What if the BST is modified (insert/delete operations) often and
you need to find the kth smallest frequently? How would you optimize
the kthSmallest routine?


Constraints:
1) The number of elements of the BST is between 1 to 10^4.
2) You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

"""

from typing import List
from heapq import *


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        min_heap = []
        in_order(root, min_heap, k)
        return min_heap[-1]


def in_order(root: TreeNode, min_heap: List[int], k: int):
    if root is None:
        return

    in_order(root.left, min_heap, k)

    if len(min_heap) < k:
        heappush(min_heap, root.val)

    in_order(root.right, min_heap, k)


def get_test_case_1() -> TreeNode:
    """
   3
  / \
 1   4
  \
   2

    :return:
    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)

    node_3.left = node_1
    node_1.right = node_2
    node_3.right = node_4

    head = node_3
    return head


def get_test_case_2() -> TreeNode:
    """
       5
      / \
     3   6
    / \
   2   4
  /
 1

    :return:
    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)

    node_5.left = node_3
    node_3.left = node_2
    node_2.left = node_1

    node_5.right = node_6
    node_3.right = node_4

    head = node_5
    return head


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.kthSmallest(get_test_case_1(), 1), 1)
    test(solution.kthSmallest(get_test_case_2(), 3), 3)
