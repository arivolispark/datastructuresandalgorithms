"""
Title:  2583. Kth Largest Sum in a Binary Tree

You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer
than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.



Example 1:
Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.


Example 2:
Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.


Constraints:
1) The number of nodes in the tree is n.
2) 2 <= n <= 10^5
3) 1 <= Node.val <= 10^6
4) 1 <= k <= n

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        result, q = [], []

        if root is None:
            return -1

        q.append(root)

        while len(q) > 0:
            level_sum = 0
            level_nodes = []

            for i in range(len(q)):
                e = q.pop(0)
                level_sum += e.val

                if e.left is not None:
                    level_nodes.append(e.left)

                if e.right is not None:
                    level_nodes.append(e.right)

            result.append(level_sum)

            for i in range(len(level_nodes)):
                q.append(level_nodes[i])

        result.sort(reverse=True)

        return result[k - 1] if (k - 1) < len(result) else -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input():
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    nine = TreeNode(9)

    five.left = eight
    five.right = nine

    eight.left = two
    eight.right = one

    two.left = four
    two.right = six

    nine.left = three
    nine.right = seven

    return five


def get_test_case_2_input():
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)

    one.left = two
    two.left = three

    return one


if __name__ == "__main__":
    solution = Solution()

    test(solution.kthLargestLevelSum(get_test_case_1_input(), 2), 13)
    test(solution.kthLargestLevelSum(get_test_case_2_input(), 1), 3)
