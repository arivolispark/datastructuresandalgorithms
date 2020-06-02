"""
Title:  Invert Binary Tree

Invert a binary tree.


Example:

Input:

    4
   /   \
  2     7
 / \   / \
1   3 6   9


Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1



Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

"""

from collections import deque
from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def in_order_traversal(root: TreeNode, result: List[int]) -> None:
    if root is None:
        return

    in_order_traversal(root.left, result)
    result.append(root.val)
    in_order_traversal(root.right, result)


def level_order_traversal(root: TreeNode, result: List[int]) -> None:
    if root is None:
        return

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        result.append(node.val)

        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


def get_test_case_1_input() -> TreeNode:
    return None


def get_test_case_1_output() -> TreeNode:
    return None


def get_test_case_2_input() -> TreeNode:
    node_1 = TreeNode(1)
    return node_1


def get_test_case_2_output() -> TreeNode:
    node_1 = TreeNode(1)
    return node_1


def get_test_case_3_input() -> TreeNode:
    """
    4
   /   \
  2     7
 / \   / \
1   3 6   9

    :return:
    """
    node_1 = TreeNode(4)
    node_2 = TreeNode(2)
    node_3 = TreeNode(7)
    node_4 = TreeNode(1)
    node_5 = TreeNode(3)
    node_6 = TreeNode(6)
    node_7 = TreeNode(9)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    return node_1


def get_test_case_3_output() -> TreeNode:
    node_1 = TreeNode(1)
    return node_1


def get_test_case_4_input() -> TreeNode:
    """
    1
   /
  2

    :return:
    """
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)

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

    """
    #print("\n Inorder traversal")
    answer = []
    #in_order_traversal(get_test_case_3_input(), answer)
    #print(" answer: ", answer)

    answer.clear()

    inverted_tree = None
    print("\n Level order traversal")
    level_order_traversal(get_test_case_3_input(), answer, inverted_tree)
    print(" answer: ", answer)

    answer.clear()

    in_order_traversal(get_test_case_3_input(), answer)
    print(" answer: ", answer)
    """

    """
    #input = get_test_case_1_input()
    #input = get_test_case_2_input()
    input = get_test_case_3_input()
    #input = get_test_case_4_input()
    #output = solution.invertTree(input)


    answer = []
    in_order_traversal(input, answer)
    print(" answer: ", answer)

    result = []
    #in_order_traversal(output, result)
    #level_order_traversal_3(input, result)
    #print(" result: ", result)

    result.clear()

    output = solution.invertTree(input)
    level_order_traversal(output, result)
    print(" result: ", result)
    """

    #test(solution.invertTree(in_order_traversal(get_test_case_1_input())), get_test_case_1_output())
    test(in_order_traversal(solution.invertTree(get_test_case_1_input()), []), in_order_traversal(solution.invertTree(get_test_case_1_output()), []))
    test(in_order_traversal(solution.invertTree(get_test_case_2_input()), []), in_order_traversal(solution.invertTree(get_test_case_2_output()), []))
    test(in_order_traversal(solution.invertTree(get_test_case_3_input()), []), in_order_traversal(solution.invertTree(get_test_case_3_output()), []))
    ##test(solution.invertTree(get_test_case_3_input()), get_test_case_3_output())
