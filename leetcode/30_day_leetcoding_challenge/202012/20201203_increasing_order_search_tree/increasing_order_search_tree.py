"""
Title:  Increasing Order Search Tree

Given the root of a binary search tree, rearrange the tree in in-order so that
the leftmost node in the tree is now the root of the tree, and every node has
no left child and only one right child.



Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]



Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]


Constraints:

1) The number of nodes in the given tree will be in the range [1, 100].
2) 0 <= Node.val <= 1000

"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder_list = []
        inorder_traversal(root, inorder_list)

        result, temp = None, None
        inorder_list_len = len(inorder_list)

        if inorder_list_len > 0:
            result = temp = TreeNode(inorder_list[0])

            for i in range(1, inorder_list_len):
                temp.right = TreeNode(inorder_list[i])
                temp = temp.right

        return result


def inorder_traversal(root: TreeNode, result: List[int]):
    if root is None:
        return
    inorder_traversal(root.left, result)
    result.append(root.val)
    inorder_traversal(root.right, result)


def preorder_traversal(root: TreeNode, result: List[int]):
    if root is None:
        return
    result.append(root.val)
    preorder_traversal(root.left, result)
    preorder_traversal(root.right, result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)

    node_5.left = node_3
    node_5.right = node_6

    node_3.left = node_2
    node_3.right = node_4

    node_2.left = node_1

    node_6.right = node_8

    node_8.left = node_7
    node_8.right = node_9

    return node_5


def get_test_case_1_output():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)

    node_1.right = node_2
    node_2.right = node_3
    node_3.right = node_4
    node_4.right = node_5
    node_5.right = node_6
    node_6.right = node_7
    node_7.right = node_8
    node_8.right = node_9

    return node_1


def get_test_case_2_input():
    node_1 = TreeNode(1)
    node_5 = TreeNode(5)
    node_7 = TreeNode(7)

    node_5.left = node_1
    node_5.right = node_7

    return node_5


def get_test_case_2_output():
    node_1 = TreeNode(1)
    node_5 = TreeNode(5)
    node_7 = TreeNode(7)

    node_1.right = node_5
    node_5.right = node_7

    return node_1


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        get_test_case_1_input(),
        get_test_case_2_input(),
    ]

    test_case_outputs = [
        get_test_case_1_output(),
        get_test_case_2_output(),
    ]

    for i in range(len(test_case_inputs)):
        result = solution.increasingBST(test_case_inputs[i])

        actual = []
        preorder_traversal(result, actual)

        expected = []
        preorder_traversal(test_case_outputs[i], expected)

        test(actual, expected)

