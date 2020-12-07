"""
Title:  Populating Next Right Pointers in Each Node II

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node.  If there is no next
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

1) You may only use constant extra space.
2) Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

1) The number of nodes in the given tree is less than 6000.
2) -100 <= node.val <= 100

"""

from typing import List
from collections import *


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])

        while q:
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if i < q_len - 1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root


def preorder_traversal(root: Node, preorder_list: List[int]):
    if root is None:
        return
    preorder_list.append(root.val)
    preorder_traversal(root.left, preorder_list)
    preorder_traversal(root.right, preorder_list)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)
    node_7 = Node(7)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.right = node_7

    return node_1


if __name__ == "__main__":
    solution = Solution()

    solution.connect(get_test_case_1_input())
