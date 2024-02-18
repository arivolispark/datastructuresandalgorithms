"""
94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]


Example 2:
Input: root = []
Output: []


Example 3:
Input: root = [1]
Output: [1]


Constraints:
1) The number of nodes in the tree is in the range [0, 100].
2) -100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import List
from typing import Optional

# Definition for a binary tree node.


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        dfs(root, result)
        return result
      
      
def dfs(root: Optional[TreeNode], result: List[int]):
    if not root:
        return None

    dfs(root.left, result)
    result.append(root.val)
    dfs(root.right, result)
    

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def test_case_1_list() -> Optional[TreeNode]:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)

    one.right = two
    two.left = three
    head1 = one

    return head1


def test_case_2_list() -> Optional[TreeNode]:
    return None


def test_case_3_list() -> Optional[TreeNode]:
    one = TreeNode(1)
    head1 = one

    return head1


if __name__ == "__main__":
    solution = Solution()

    result1 = solution.inorderTraversal(test_case_1_list())
    result2 = solution.inorderTraversal(test_case_2_list())
    result3 = solution.inorderTraversal(test_case_3_list())

    test(result1, [1,3,2])
    test(result2, [])
    test(result3, [1])
