"""
Title:  Construct Binary Search Tree from Preorder Traversal

Return the root node of a binary search tree that matches the
given preorder traversal.

(Recall that a binary search tree is a binary tree where for every
node, any descendant of node.left has a value < node.val, and any
descendant of node.right has a value > node.val.  Also recall that a
preorder traversal displays the value of the node first, then
traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible
to find a binary search tree with the given requirements.

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]


Constraints:
1) 1 <= preorder.length <= 100
2) 1 <= preorder[i] <= 10^8
3) The values of preorder are distinct.

"""

from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder:
            n = len(preorder)
            if n == 1:
                return TreeNode(preorder[0])
            else:
                root = None
                i = 0
                while i < n:
                    temp = TreeNode(preorder[i])
                    if root is None:
                        root = temp
                    else:
                        node = root

                        while node:
                            if preorder[i] < node.val:
                                if node.left:
                                    node = node.left
                                else:
                                    node.left = temp
                                    break
                            elif preorder[i] > node.val:
                                if node.right:
                                    node = node.right
                                else:
                                    node.right = temp
                                    break
                    i += 1
                return root
        return None


def inorder(root: TreeNode, result: List[int]) -> None:
    if root is None:
        return
    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)


def preorder(root: TreeNode, result: List[int]) -> None:
    if root is None:
        return
    result.append(root.val)
    preorder(root.left, result)
    preorder(root.right, result)


def postorder(root: TreeNode, result: List[int]) -> None:
    if root is None:
        return
    postorder(root.left, result)
    postorder(root.right, result)
    result.append(root.val)


def get_test_case_1() -> TreeNode:
    node_10 = TreeNode(10)
    node_20 = TreeNode(20)
    node_30 = TreeNode(30)
    node_40 = TreeNode(40)
    node_50 = TreeNode(50)

    node_30.left = node_20
    node_20.left = node_10
    node_30.right = node_40
    node_40.right = node_50

    return node_30


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    """
    root = get_test_case_1()

    inorder_result = []
    inorder(root, inorder_result)
    print("\n inorder_result: ", inorder_result)

    preorder_result = []
    preorder(root, preorder_result)
    print(" preorder_result: ", preorder_result)

    postorder_result = []
    postorder(root, postorder_result)
    print(" postorder_result: ", postorder_result)
    """

    preorder_input_1 = [8,5,1,7,10,12]
    print("\n preorder_input_1: ", preorder_input_1)

    bst_root_1 = solution.bstFromPreorder(preorder_input_1)

    inorder_result = []
    inorder(bst_root_1, inorder_result)
    print("\n inorder_result: ", inorder_result)

    preorder_result = []
    preorder(bst_root_1, preorder_result)
    print(" preorder_result: ", preorder_result)

    postorder_result = []
    postorder(bst_root_1, postorder_result)
    print(" postorder_result: ", postorder_result)


    #test(solution.bstFromPreorder(None), None)
    #test(solution.bstFromPreorder([]), None)
    #test(solution.bstFromPreorder([8]), None)
