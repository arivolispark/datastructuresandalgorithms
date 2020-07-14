"""
Title:  Same Tree

Given two binary trees, write a function to check if
they are the same or not.

Two binary trees are considered the same if they are
structurally identical and the nodes have the same value.


Example 1:
Input:
           1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true



Example 2:
Input:
           1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false



Example 3:
Input:
           1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def get_test_case_1() -> (TreeNode, TreeNode):
    return None, None


def get_test_case_2() -> (TreeNode, TreeNode):
    return TreeNode(1), None


def get_test_case_3() -> (TreeNode, TreeNode):
    return None, TreeNode(1)


def get_test_case_4() -> (TreeNode, TreeNode):
    """
           1         1
          / \       / \
         2   3     2   3

    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)

    node_1.left = node_2
    node_1.right = node_3

    head_1 = node_1

    return head_1, head_1


def get_test_case_5() -> (TreeNode, TreeNode):
    """
           1         1
          /           \
         2             2

    """

    node_11 = TreeNode(1)
    node_12 = TreeNode(2)

    node_11.left = node_12

    head_1 = node_11

    node_21 = TreeNode(1)
    node_22 = TreeNode(2)

    node_21.right = node_22

    head_2 = node_21

    return head_1, head_2


def get_test_case_6() -> (TreeNode, TreeNode):
    """
           1         1
          / \       / \
         2   1     1   2

    """

    node_11 = TreeNode(1)
    node_12 = TreeNode(2)
    node_13 = TreeNode(1)

    node_11.left = node_12
    node_11.right = node_13

    head_1 = node_11

    node_21 = TreeNode(1)
    node_22 = TreeNode(1)
    node_23 = TreeNode(2)

    node_21.left = node_22
    node_21.right = node_23

    head_2 = node_21

    return head_1, head_2


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.isSameTree(get_test_case_1()[0], get_test_case_1()[1]), True)
    test(solution.isSameTree(get_test_case_2()[0], get_test_case_2()[1]), False)
    test(solution.isSameTree(get_test_case_3()[0], get_test_case_3()[1]), False)
    test(solution.isSameTree(get_test_case_4()[0], get_test_case_4()[1]), True)
    test(solution.isSameTree(get_test_case_5()[0], get_test_case_5()[1]), False)
    test(solution.isSameTree(get_test_case_6()[0], get_test_case_6()[1]), False)
