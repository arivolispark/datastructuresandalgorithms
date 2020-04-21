"""
Title:  Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for
every node, any descendant of node.left has a value < node.val, and
any descendant of node.right has a value > node.val.  Also recall that
a preorder traversal displays the value of the node first, then traverses
node.left, then traverses node.right.)


Example 1:


             8
           /  \
          /    \
        5       10
       /  \       \
      /    \       \
    1       7       12



Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]


Note:
    1) 1 <= preorder.length <= 100
    2) The values of preorder are distinct.
"""

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder and len(preorder) > 0:
            n = len(preorder)
            if n == 1:
                return TreeNode(preorder[0])
            else:
                root = None
                for value in preorder:
                    if root is None:
                        root = TreeNode(value)
                    else:
                        node = root
                        while node:
                            if value < node.val:
                                if node.left:
                                    node = node.left
                                else:
                                    node.left = TreeNode(value)
                                    break
                            else:
                                if node.right:
                                    node = node.right
                                else:
                                    node.right = TreeNode(value)
                                    break
                return root
        else:
            return None


def in_order_traversal(root: TreeNode) -> None:
    if root is None:
        return
    in_order_traversal(root.left)
    print(root.val, end=" ")
    in_order_traversal(root.right)


def pre_order_traversal(root: TreeNode) -> None:
    if root is None:
        return
    print(root.val, end=" ")
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)


def post_order_traversal(root: TreeNode) -> None:
    if root is None:
        return
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.val, end=" ")


def level_order_traversal(root: TreeNode):
    level_order_traversal_result = []
    queue = deque()
    if root is None:
        return []
    else:
        queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()
        if node is not None:
            level_order_traversal_result.append(node.val)
            if node.left or node.right:
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)

                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
        else:
            level_order_traversal_result.append(None)
    return level_order_traversal_result


def get_test_case_1() -> (List[int]):
    return None


def get_test_case_2() -> (List[int]):
    return []


def get_test_case_3() -> (List[int]):
    return [14]


def get_test_case_4() -> (List[int]):
    return [8, 5, 1, 7, 10, 12]


def get_test_case_5() -> (List[int]):
    return [30, 20, 10, 40, 50]


if __name__ == "__main__":
    solution = Solution()

    #preorder = get_test_case_1()
    #preorder = get_test_case_2()
    #preorder = get_test_case_3()
    preorder = get_test_case_4()
    #preorder = get_test_case_5()
    print("\n preorder: ", preorder)

    root = solution.bstFromPreorder(preorder)

    print("\n\n In-order traversal")
    in_order_traversal(root)

    print("\n\n Pre-order traversal")
    pre_order_traversal(root)

    print("\n\n Post-order traversal")
    post_order_traversal(root)

    print("\n\n Level-order traversal")
    level_order_traversal_result = level_order_traversal(root)
    print(" level_order_traversal_result: ", level_order_traversal_result)
