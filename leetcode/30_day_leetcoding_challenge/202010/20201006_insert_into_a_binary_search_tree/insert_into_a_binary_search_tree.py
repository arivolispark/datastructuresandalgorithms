"""
Title:  Insert into a Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the
root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after
insertion. You can return any of them.



Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:


Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]


Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]


Constraints:
1) The number of nodes in the tree will be in the range [0, 104].
2) -10 ^ 8 <= Node.val <= 10 ^ 8
3) All the values Node.val are unique.
4) -10 ^ 8 <= val <= 10 ^ 8
5) It's guaranteed that val does not exist in the original BST.


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


def get_test_case_1_input():
    """
    Input: root = [4,2,7,1,3], val = 5

          4
        /  \
       2    7
     /  \
    1    3

    :return:
    """

    node_1 = TreeNode(4)
    node_2 = TreeNode(2)
    node_3 = TreeNode(7)
    node_4 = TreeNode(1)
    node_5 = TreeNode(3)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5

    head = node_1
    return head


def get_test_case_2_input():
    """
    Input: root = [40,20,60,10,30,50,70], val = 25

           40
         /    \
      20       60
     /  \      / \
   10    30   50  70

    :return:
    """

    node_1 = TreeNode(40)
    node_2 = TreeNode(20)
    node_3 = TreeNode(60)
    node_4 = TreeNode(10)
    node_5 = TreeNode(30)
    node_6 = TreeNode(50)
    node_7 = TreeNode(70)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    head = node_1
    return head


def get_test_case_3_input():
    """
    Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5

          4
        /  \
       2    7
     /  \
    1    3

    :return:
    """

    node_1 = TreeNode(4)
    node_2 = TreeNode(2)
    node_3 = TreeNode(7)
    node_4 = TreeNode(1)
    node_5 = TreeNode(3)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5

    head = node_1
    return head


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()
