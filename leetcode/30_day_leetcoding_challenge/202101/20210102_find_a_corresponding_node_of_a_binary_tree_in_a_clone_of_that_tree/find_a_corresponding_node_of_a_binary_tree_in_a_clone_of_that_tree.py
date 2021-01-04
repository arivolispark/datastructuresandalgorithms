"""
Title:  Find a Corresponding Node of a Binary Tree in a Clone of That Tree

Given two binary trees original and cloned and given a reference to a node target
in the original tree.

The cloned tree is a copy of the original tree.  Return a reference to the same node
in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and
the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.



Example 1:


Input: tree = [7,4,3,null,null,6,19], target = 3
Output: 3
Explanation: In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.



Example 2:


Input: tree = [7], target =  7
Output: 7



Example 3:


Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
Output: 4



Example 4:


Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
Output: 5



Example 5:


Input: tree = [1,2,null,3], target = 2
Output: 2


Constraints:

1) The number of nodes in the tree is in the range [1, 10^4].
2) The values of the nodes of the tree are unique.
3) target node is a node from the original tree and is not null.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original or original == target:
            return cloned

        result = self.getTargetCopy(original.left, cloned.left, target)
        if result:
            return result
        return self.getTargetCopy(original.right, cloned.right, target)


def get_test_case_1_input():
    node_7 = TreeNode(7)
    node_4 = TreeNode(4)
    node_3 = TreeNode(3)
    node_6 = TreeNode(6)
    node_19 = TreeNode(19)

    node_7.left = node_4
    node_7.right = node_3

    node_3.left = node_6
    node_3.right = node_19

    head = node_7
    return head


def get_test_case_1_target():
    return TreeNode(3)


def get_test_case_2_input():
    node_7 = TreeNode(7)

    head = node_7
    return head


def get_test_case_2_target():
    return TreeNode(7)


def get_test_case_3_input():
    node_8 = TreeNode(8)
    node_6 = TreeNode(6)
    node_5 = TreeNode(5)
    node_4 = TreeNode(4)
    node_3 = TreeNode(3)
    node_2 = TreeNode(2)
    node_1 = TreeNode(1)

    node_8.right = node_6
    node_6.right = node_5
    node_5.right = node_4
    node_4.right = node_3
    node_3.right = node_2
    node_2.right = node_1

    head = node_8
    return head


def get_test_case_3_target():
    return TreeNode(4)


def get_test_case_4_input():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)
    node_10 = TreeNode(10)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_4.left = node_8
    node_4.right = node_9

    node_5.left = node_10

    node_3.left = node_6
    node_3.right = node_7

    head = node_1
    return head


def get_test_case_4_target():
    return TreeNode(5)


def get_test_case_5_input():
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)

    node_1.left = node_2
    node_2.left = node_3

    head = node_1
    return head


def get_test_case_5_target():
    return TreeNode(2)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    # test(solution.getTargetCopy(get_test_case_1_input(), get_test_case_1_input(), get_test_case_1_target()), get_test_case_1_target())
    # test(solution.getTargetCopy(get_test_case_2_input(), get_test_case_2_input(), get_test_case_2_target()).val, get_test_case_2_target().val)
    # test(solution.getTargetCopy(get_test_case_3_input(), get_test_case_3_input(), get_test_case_3_target()).val, get_test_case_3_target().val)
    # test(solution.getTargetCopy(get_test_case_4_input(), get_test_case_4_input(), get_test_case_4_target()).val, get_test_case_4_target().val)
    # test(solution.getTargetCopy(get_test_case_5_input(), get_test_case_5_input(), get_test_case_5_target()).val, get_test_case_5_target().val)
