"""
Title:  Search in a Binary Search Tree

Given the root node of a binary search tree (BST) and a value. You
need to find the node in the BST that the node's value equals the
given value. Return the subtree rooted with that node. If such node
doesn't exist, you should return NULL.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2


You should return this subtree:

      2
     / \
    1   3


In the example above, if we want to search the value 5, since there
is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would
see the expected output (serialized tree format) as [], not null.

"""

from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
        else:
            return None


def inorder(root: TreeNode, result: List[int]):
    if root is None:
        return
    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input() -> TreeNode:
    """

        4
       / \
      2   7
     / \
    1   3

    """

    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    seven = TreeNode(7)

    four.left = two
    four.right = seven

    two.left = one
    two.right = three

    root = four

    return root


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        [None, None],
        [None, 10],
        [get_test_case_1_input(), 2],
        [get_test_case_1_input(), 100],
        [get_test_case_1_input(), 4],
        [get_test_case_1_input(), 1],
        [get_test_case_1_input(), 3]
    ]

    test_case_outputs = [
        [],
        [],
        [1, 2, 3],
        [],
        [1, 2, 3, 4, 7],
        [1],
        [3]
    ]

    for i in range(len(test_case_inputs)):
        output = solution.searchBST(test_case_inputs[i][0], test_case_inputs[i][1])
        output_list = []
        inorder(output, output_list)
        test(test_case_outputs[i], output_list)
