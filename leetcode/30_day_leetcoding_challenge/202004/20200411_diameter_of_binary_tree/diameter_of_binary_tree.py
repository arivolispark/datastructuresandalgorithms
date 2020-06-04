"""
Title:  Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree.  This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \
      4  5


Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

"""


# Definition for a binary tree node.
class TreeNode:

     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, node: TreeNode) -> int:
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.diameter = max(self.diameter, left + right)
        return max(left + 1, right + 1)


def inorder_traversal(root: TreeNode) -> None:
    if root is None:
        return

    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)


def get_empty_binary_tree() -> TreeNode:
    return None


def get_single_node_binary_tree() -> TreeNode:
    one = TreeNode(1)
    return one


def get_left_skewed_binary_tree_1() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    one.left = two
    return one


def get_left_skewed_binary_tree_2() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)

    one.left = two
    two.left = three
    return one


def get_left_skewed_binary_tree_3() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)

    one.left = two
    two.left = three
    three.left = four
    return one


def get_left_skewed_binary_tree_4() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    one.left = two
    two.left = three
    three.left = four
    four.left = five
    return one


def get_left_skewed_binary_tree_5() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)

    one.left = two
    two.left = three
    three.left = four
    four.left = five
    five.left = six
    return one


def get_left_skewed_binary_tree_6() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)

    one.left = two
    two.left = three
    three.left = four
    four.left = five
    five.left = six
    six.left = seven
    return one


def get_right_skewed_binary_tree_1() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    one.right = two
    return one


def get_right_skewed_binary_tree_2() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)

    one.right = two
    two.right = three
    return one


def get_right_skewed_binary_tree_3() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)

    one.right = two
    two.right = three
    three.right = four
    return one


def get_right_skewed_binary_tree_4() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    one.right = two
    two.right = three
    three.right = four
    four.right = five
    return one


def get_right_skewed_binary_tree_5() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)

    one.right = two
    two.right = three
    three.right = four
    four.right = five
    five.right = six
    return one


def get_right_skewed_binary_tree_6() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)

    one.right = two
    two.right = three
    three.right = four
    four.right = five
    five.right = six
    six.right = seven
    return one


def get_binary_tree_test_case_1() -> TreeNode:
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    one.left = two
    one.right = three
    two.left = four
    two.right = five
    return one


def get_binary_tree_test_case_2() -> TreeNode:
    node_1 = TreeNode(4)
    node_2 = TreeNode(-7)
    node_3 = TreeNode(-3)
    node_4 = TreeNode(-9)
    node_5 = TreeNode(9)
    node_6 = TreeNode(6)
    node_7 = TreeNode(0)
    node_8 = TreeNode(-1)
    node_9 = TreeNode(6)
    node_10 = TreeNode(-4)
    node_11 = TreeNode(-7)
    node_12 = TreeNode(-6)
    node_13 = TreeNode(5)
    node_14 = TreeNode(-6)
    node_15 = TreeNode(9)
    node_16 = TreeNode(-2)
    node_17 = TreeNode(-3)
    node_18 = TreeNode(-4)

    node_1.left = node_2
    node_1.right = node_3
    node_3.left = node_4
    node_4.left = node_5

    node_5.left = node_6
    node_6.left = node_7
    node_7.right = node_8
    node_6.right = node_9

    node_9.left = node_10
    node_4.right = node_11
    node_11.left = node_12
    node_12.left = node_13

    node_11.right = node_14
    node_14.left = node_15
    node_15.left = node_16
    node_3.right = node_17

    node_17.right = node_18

    return node_1


if __name__ == "__main__":
    solution = Solution()

    #root = get_empty_binary_tree()

    #root = get_single_node_binary_tree()

    #root = get_left_skewed_binary_tree_1()
    #root = get_left_skewed_binary_tree_2()
    #root = get_left_skewed_binary_tree_3()
    #root = get_left_skewed_binary_tree_4()
    #root = get_left_skewed_binary_tree_5()
    #root = get_left_skewed_binary_tree_6()

    #root = get_right_skewed_binary_tree_1()
    #root = get_right_skewed_binary_tree_2()
    #root = get_right_skewed_binary_tree_3()
    #root = get_right_skewed_binary_tree_4()
    #root = get_right_skewed_binary_tree_5()
    #root = get_right_skewed_binary_tree_6()

    #root = get_binary_tree_test_case_1()
    root = get_binary_tree_test_case_2()

    print("\n\n Inorder traversal")
    inorder_traversal(root)

    binary_tree_diameter =  solution.diameterOfBinaryTree(root)
    print("\n\n binary_tree_diameter: ", binary_tree_diameter)
