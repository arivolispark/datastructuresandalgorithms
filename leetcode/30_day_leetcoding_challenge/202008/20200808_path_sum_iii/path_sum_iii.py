"""
Title:  Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the
range -1,000,000 to 1,000,000.


Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> int:
        def helper(root: TreeNode, sum: int):
            if root is None:
                return 0
            result = 0
            if root.val == sum:
                result += 1
            result += helper(root.left, sum - root.val)
            result += helper(root.right, sum - root.val)
            return result
        if root is None:
            return 0
        return self.pathSum(root.left, sum) + helper(root, sum) + self.pathSum(root.right, sum)


def get_test_case_1_input() -> TreeNode:
    """

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

    """

    node_1 = TreeNode(10)
    node_2 = TreeNode(5)
    node_3 = TreeNode(-3)
    node_4 = TreeNode(3)
    node_5 = TreeNode(2)
    node_6 = TreeNode(11)
    node_7 = TreeNode(3)
    node_8 = TreeNode(-2)
    node_9 = TreeNode(1)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.right = node_6

    node_4.left = node_7
    node_4.right = node_8

    node_5.right = node_9

    return node_1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        get_test_case_1_input(),
    ]

    test_case_sums = [
        8,
    ]

    test_case_outputs = [
        3,
    ]

    for i in range(len(test_case_inputs)):
        test(solution.pathSum(test_case_inputs[i], test_case_sums[i]), test_case_outputs[i])
