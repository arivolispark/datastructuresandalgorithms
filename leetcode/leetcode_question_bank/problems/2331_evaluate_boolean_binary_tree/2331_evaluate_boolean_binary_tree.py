"""
Title:  2331. Evaluate Boolean Binary Tree

You are given the root of a full binary tree with the following properties:

1) Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
2) Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.


The evaluation of a node is as follows:
1) If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
2) Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.

Return the boolean result of evaluating the root node.


A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.


Example 1:
Input: root = [2,1,3,null,null,0,1]
Output: true
Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.


Example 2:
Input: root = [0]
Output: false
Explanation: The root node is a leaf node and it evaluates to false, so we return false.


Constraints:
1) The number of nodes in the tree is in the range [1, 1000].
2) 0 <= Node.val <= 3
3) Every node has either 0 or 2 children.
4) Leaf nodes have a value of 0 or 1.
5) Non-leaf nodes have a value of 2 or 3.

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if root.left is None and root.right is None:
                return bool(root.val)

            l = dfs(root.left)
            r = dfs(root.right)
            return (l or r) if root.val == 2 else (l and r)

        return dfs(root)


def get_test_case_1_input():
    one = TreeNode(2)
    two = TreeNode(1)
    three = TreeNode(3)
    four = TreeNode(0)
    five = TreeNode(1)

    one.left = two
    one.right = three
    three.left = four
    three.right = five

    root = one
    return root


def get_test_case_2_input():
    one = TreeNode(0)

    root = one
    return root


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.evaluateTree(get_test_case_1_input()), True)
    test(solution.evaluateTree(get_test_case_2_input()), False)
