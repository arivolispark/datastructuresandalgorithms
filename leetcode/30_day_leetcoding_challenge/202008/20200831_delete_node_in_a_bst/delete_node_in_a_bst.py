"""
Title:  Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the
given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
1) Search for a node to remove.
2) If the node is found, delete the node.

Note: Time complexity should be O(height of tree).


Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7


"""


from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root

        def inorder_predecessor(root):
            root = root.left
            while root.right is not None:
                root = root.right
            return root.val

        def inorder_successor(root):
            root = root.right
            while root.left is not None:
                root = root.left
            return root.val

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left is not None:
                root.val = inorder_predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                root.val = inorder_successor(root)
                root.right = self.deleteNode(root.right, root.val)
        return root


def get_test_case_1_input():
    """
      5
     / \
    3   6
   / \   \
  2   4   7

    :return:
    """

    node_5 = TreeNode(5)
    node_3 = TreeNode(3)
    node_6 = TreeNode(6)
    node_2 = TreeNode(2)
    node_4 = TreeNode(4)
    node_7 = TreeNode(7)

    node_5.left = node_3
    node_5.right = node_6
    node_3.left = node_2
    node_3.right = node_4
    node_6.right = node_7

    head = node_5
    return head


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    #test(solution.deleteNode(get_test_case_1_input(), 3), [-1])
