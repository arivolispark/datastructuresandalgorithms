"""
Title:  Sum of Root To Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a
binary number starting with the most significant bit.  For example, if the path
is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the
root to that leaf.

Return the sum of these numbers.



Example 1:
                  1
                /   \
               0     1
             /  \   /  \
            0   1  0    1


Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


Note:
1) The number of nodes in the tree is between 1 and 1000.
2) node.val is 0 or 1.
3) The answer will not exceed 2^31 - 1.

"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:
        def sum_root_to_leaf(root, sum):
            if root is None:
                return 0

            sum = (sum << 1) + root.val
            if root.left is None and root.right is None:
                return sum
            return sum_root_to_leaf(root.left, sum) + sum_root_to_leaf(root.right, sum)
        return sum_root_to_leaf(root, 0)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input() -> TreeNode:
    """
                  1
                /   \
               0     1
             /  \   /  \
            0   1  0    1

    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(0)
    node_3 = TreeNode(1)
    node_4 = TreeNode(0)
    node_5 = TreeNode(1)
    node_6 = TreeNode(0)
    node_7 = TreeNode(1)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    head = node_1
    return head


def get_test_case_1_output() -> int:
    return 22


if __name__ == "__main__":
    solution = Solution()

    test(solution.sumRootToLeaf(get_test_case_1_input()), get_test_case_1_output())

