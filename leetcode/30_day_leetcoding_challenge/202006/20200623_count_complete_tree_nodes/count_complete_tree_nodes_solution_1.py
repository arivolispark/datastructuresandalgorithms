"""
Title:  Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely
filled, and all nodes in the last level are as far left as possible. It can have
between 1 and 2h nodes inclusive at the last level h.

Example:

Input:

    1
   / \
  2   3
 / \  /
4  5 6

Output: 6


"""

from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def countNodes(self, root: TreeNode) -> int:
        result, left, right = [], [], []
        post_order_traversal_1(root, result, left, right)
        print("\n result: ", result)
        print(" left: ", left)
        print(" right: ", right)
        return len(result)


def post_order_traversal(root: TreeNode, result: List[int]):
    if root is None:
        return
    post_order_traversal(root.left, result)
    post_order_traversal(root.right, result)
    result.append(root.val)


def post_order_traversal_1(root: TreeNode, result: List[int], left: List[int], right: List[int]):
    if root is None:
        return
    post_order_traversal_1(root.left, result, left, right)
    post_order_traversal_1(root.right, result, left, right)
    result.append(root.val)
    if root.left:
        left.append(root.left.val)
    if root.right:
        right.append(root.right.val)


def get_test_case_1_input() -> TreeNode:
    return None


def get_test_case_2_input() -> TreeNode:
    return TreeNode(1)


def get_test_case_3_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)

    one.left = two

    head = one
    return head


def get_test_case_4_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)

    one.left = two
    one.right = three

    head = one
    return head


def get_test_case_5_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)

    one.left = two
    one.right = three

    two.left = four

    head = one
    return head


def get_test_case_6_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    head = one
    return head


def get_test_case_7_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six

    head = one
    return head


def get_test_case_8_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six
    three.right = seven

    head = one
    return head


def get_test_case_9_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six
    three.right = seven

    four.left = eight

    head = one
    return head


def get_test_case_10_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    nine = TreeNode(9)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six
    three.right = seven

    four.left = eight
    four.right = nine

    head = one
    return head


def get_test_case_11_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    nine = TreeNode(9)
    ten = TreeNode(10)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six
    three.right = seven

    four.left = eight
    four.right = nine

    five.left = ten

    head = one
    return head


def get_test_case_12_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    nine = TreeNode(9)
    ten = TreeNode(10)
    eleven = TreeNode(11)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six
    three.right = seven

    four.left = eight
    four.right = nine

    five.left = ten
    five.right = eleven

    head = one
    return head


def get_test_case_13_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    nine = TreeNode(9)
    ten = TreeNode(10)
    eleven = TreeNode(11)
    twelve = TreeNode(12)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six
    three.right = seven

    four.left = eight
    four.right = nine

    five.left = ten
    five.right = eleven

    six.left = twelve

    head = one
    return head


def get_test_case_14_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    nine = TreeNode(9)
    ten = TreeNode(10)
    eleven = TreeNode(11)
    twelve = TreeNode(12)
    thirty = TreeNode(13)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six
    three.right = seven

    four.left = eight
    four.right = nine

    five.left = ten
    five.right = eleven

    six.left = twelve
    six.right = thirty

    head = one
    return head


def get_test_case_15_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    nine = TreeNode(9)
    ten = TreeNode(10)
    eleven = TreeNode(11)
    twelve = TreeNode(12)
    thirty = TreeNode(13)
    fourteen = TreeNode(14)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six
    three.right = seven

    four.left = eight
    four.right = nine

    five.left = ten
    five.right = eleven

    six.left = twelve
    six.right = thirty

    seven.left = fourteen

    head = one
    return head


def get_test_case_16_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    nine = TreeNode(9)
    ten = TreeNode(10)
    eleven = TreeNode(11)
    twelve = TreeNode(12)
    thirty = TreeNode(13)
    fourteen = TreeNode(14)
    fifteen = TreeNode(15)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six
    three.right = seven

    four.left = eight
    four.right = nine

    five.left = ten
    five.right = eleven

    six.left = twelve
    six.right = thirty

    seven.left = fourteen
    seven.right = fifteen

    head = one
    return head


def get_test_case_17_input() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)

    one.left = two
    one.right = three

    two.left = four
    two.right = five

    three.left = six

    head = one

    return head


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    """
    test(solution.countNodes(get_test_case_1_input()), 0)
    test(solution.countNodes(get_test_case_2_input()), 1)
    test(solution.countNodes(get_test_case_3_input()), 2)
    test(solution.countNodes(get_test_case_4_input()), 3)
    test(solution.countNodes(get_test_case_5_input()), 4)
    test(solution.countNodes(get_test_case_6_input()), 5)
    test(solution.countNodes(get_test_case_7_input()), 6)
    test(solution.countNodes(get_test_case_8_input()), 7)
    test(solution.countNodes(get_test_case_9_input()), 8)
    test(solution.countNodes(get_test_case_10_input()), 9)
    test(solution.countNodes(get_test_case_11_input()), 10)
    test(solution.countNodes(get_test_case_12_input()), 11)
    test(solution.countNodes(get_test_case_13_input()), 12)
    test(solution.countNodes(get_test_case_14_input()), 13)
    test(solution.countNodes(get_test_case_15_input()), 14)
    """
    test(solution.countNodes(get_test_case_16_input()), 15)
    #test(solution.countNodes(get_test_case_17_input()), 6)
