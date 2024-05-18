"""
Title:  979. Distribute Coins in Binary Tree

You are given the root of a binary tree with n nodes where each node in the tree
has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node
to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.



Example 1:
Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.


Example 2:
Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.


Constraints:
1) The number of nodes in the tree is n.
2) 1 <= n <= 100
3) 0 <= Node.val <= n
4) The sum of all Node.val is n.

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.number_of_moves = 0

        def dfs(node):
            if node is None:
                return 0

            l_balance, r_balance = dfs(node.left), dfs(node.right)
            self.number_of_moves += abs(l_balance) + abs(r_balance)
            return node.val + l_balance + r_balance - 1

        dfs(root)
        return self.number_of_moves


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input():
    one = TreeNode(3)
    two = TreeNode(0)
    three = TreeNode(0)

    one.left = two
    one.right = three

    root = one
    return root


def get_test_case_2_input():
    one = TreeNode(0)
    two = TreeNode(3)
    three = TreeNode(0)

    one.left = two
    one.right = three

    root = one
    return root


if __name__ == "__main__":
    solution = Solution()

    test(solution.distributeCoins(get_test_case_1_input()), 2)
    test(solution.distributeCoins(get_test_case_2_input()), 3)
