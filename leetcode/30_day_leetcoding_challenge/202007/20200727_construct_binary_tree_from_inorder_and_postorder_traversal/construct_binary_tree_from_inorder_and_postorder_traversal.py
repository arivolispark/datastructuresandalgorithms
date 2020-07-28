"""
Title:  Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]


Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            n = len(inorder)
            if n == 0:
                return None
            self.inorder = inorder
            self.postorder = postorder
            return self.build_tree_recursive(0, n, 0, n)
        return None

    def build_tree_recursive(self, inorder1, inorder2, postorder1, postorder2):
        if inorder1 >= inorder2 or postorder1 >= postorder2:
            return None
        root = TreeNode(self.postorder[postorder2 - 1])
        it = self.inorder.index(self.postorder[postorder2 - 1])
        diff = it - inorder1
        root.left = self.build_tree_recursive(inorder1, inorder1 + diff, postorder1, postorder1 + diff)
        root.right = self.build_tree_recursive(inorder1 + diff + 1, inorder2, postorder1 + diff, postorder2 - 1)
        return root


def inorder_traversal(root: TreeNode, result: List[int]):
    if root is None:
        return
    inorder_traversal(root.left, result)
    result.append(root.val)
    inorder_traversal(root.right, result)


def get_test_case_1_output() -> TreeNode:
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


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        [[9,3,15,20,7], [9,15,7,20,3]]
    ]

    for i in range(len(test_case_inputs)):
        result_binary_tree = solution.buildTree(test_case_inputs[i][0], test_case_inputs[i][1])
        result = []
        inorder_traversal(result_binary_tree, result)

        test(test_case_inputs[i][0], result)
