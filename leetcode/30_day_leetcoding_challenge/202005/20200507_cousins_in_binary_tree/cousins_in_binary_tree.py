"""
Title:  Cousins in Binary Tree

In a binary tree, the root node is at depth 0, and children
of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same
depth, but have different parents.

We are given the root of a binary tree with unique values, and
the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the
values x and y are cousins.


Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false


Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true


Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false


Note:
1) The number of nodes in the tree will be between 2 and 100.
2) Each node has a unique integer value from 1 to 100.

"""

from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False

        x_parent, y_parent = None, None
        q = []
        root_parent = TreeNode(-1)

        q.append((root, root_parent))

        while len(q) > 0:
            levSize = len(q)
            while levSize:
                node = q.pop(0)

                if node[0].val == x:
                    x_parent = node[1]

                if node[0].val == y:
                    y_parent = node[1]

                if node[0].left:
                    q.append((node[0].left, node[0]))

                if node[0].right:
                    q.append((node[0].right, node[0]))

                levSize -= 1

                if x_parent and y_parent:
                    break

            if x_parent and y_parent:
                return x_parent != y_parent

            if (x_parent and not y_parent) or (y_parent and not x_parent):
                return False

        return False


def inorder_traversal(root: TreeNode):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)


def level_order_traversal(root: TreeNode):
    q = deque()
    if root:
        q.append(root)

        while len(q) > 0:
            node = q.popleft()
            print(node.val, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1() -> (TreeNode, int, int):
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4

    head = node_1
    x = 4
    y = 3

    return head, x, y


def get_test_case_2() -> (TreeNode, int, int):
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)

    node_1.left = node_2
    node_1.right = node_3

    node_2.right = node_4

    node_3.right = node_5

    head = node_1
    x = 5
    y = 4

    return head, x, y


def get_test_case_3() -> (TreeNode, int, int):
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)

    node_1.left = node_2
    node_1.right = node_3

    node_2.right = node_4

    head = node_1
    x = 2
    y = 3

    return head, x, y


if __name__ == "__main__":
    solution = Solution()

    root, x, y = get_test_case_1()
    test(solution.isCousins(root, x, y), False)

    root, x, y = get_test_case_2()
    test(solution.isCousins(root, x, y), True)

    root, x, y = get_test_case_3()
    test(solution.isCousins(root, x, y), False)
