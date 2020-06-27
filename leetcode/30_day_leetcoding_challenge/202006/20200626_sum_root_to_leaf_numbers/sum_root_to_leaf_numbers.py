"""
Title:  Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only,
each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which
represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.


Example 1:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.


Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumNumbers(self, root: TreeNode) -> int:
        return helper(root, 0)


def helper(root: TreeNode, result: int):
    if root is None:
        return 0
    else:
        result = 10 * result + root.val

        if root.left is None and root.right is None:
            return result
        return helper(root.left, result) + helper(root.right, result)


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
    """
        4
       / \
      9   0
     / \
    5   1


    :return:
    """
    four = TreeNode(4)
    nine = TreeNode(9)
    zero = TreeNode(0)
    five = TreeNode(5)
    one = TreeNode(1)

    four.left = nine
    four.right = zero

    nine.left = five
    nine.right = one

    head = four
    return head


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.sumNumbers(get_test_case_1_input()), 0)
    test(solution.sumNumbers(get_test_case_2_input()), 1)
    test(solution.sumNumbers(get_test_case_3_input()), 12)
    test(solution.sumNumbers(get_test_case_4_input()), 25)
    test(solution.sumNumbers(get_test_case_5_input()), 1026)
