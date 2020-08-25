"""
Title:  Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.


Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum_of_left_leaves = 0

        def sumOfLeftLeaves(root: TreeNode, is_left) -> int:
            if is_left and root.left is None and root.right is None:
                self.sum_of_left_leaves += root.val
                return
            if root.left is not None:
                sumOfLeftLeaves(root.left, True)
            if root.right is not None:
                sumOfLeftLeaves(root.right, False)

        if root is None:
            return 0
        sumOfLeftLeaves(root, False)

        return self.sum_of_left_leaves


def get_test_case_1():
    return None


def get_test_case_2():
    """
     3
    """

    node_1 = TreeNode(3)
    head = node_1

    return head


def get_test_case_3():
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


def get_test_case_4():
    """
     1
      \
      2

    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)

    node_1.right = node_2

    head = node_1

    return head


def get_test_case_5():
    """
        1
      /  \
     2    3
   /  \
  4    5
    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    head = node_1

    return head


def get_test_case_6():
    """
              0
            /   \
         2       4
       /        /  \
      1        3   -1
     / \        \    \
    5   1        6    8
    """

    node_1 = TreeNode(0)
    node_2 = TreeNode(2)
    node_3 = TreeNode(4)
    node_4 = TreeNode(1)
    node_5 = TreeNode(3)
    node_6 = TreeNode(-1)
    node_7 = TreeNode(5)
    node_8 = TreeNode(1)
    node_9 = TreeNode(6)
    node_10 = TreeNode(8)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4

    node_3.left = node_5
    node_3.right = node_6

    node_4.left = node_7
    node_4.right = node_8

    node_5.right = node_9
    node_6.right = node_10

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

    test(solution.sumOfLeftLeaves(get_test_case_1()), 0)
    test(solution.sumOfLeftLeaves(get_test_case_2()), 0)
    test(solution.sumOfLeftLeaves(get_test_case_3()), 24)
    test(solution.sumOfLeftLeaves(get_test_case_4()), 0)
    test(solution.sumOfLeftLeaves(get_test_case_5()), 4)
    test(solution.sumOfLeftLeaves(get_test_case_6()), 5)
