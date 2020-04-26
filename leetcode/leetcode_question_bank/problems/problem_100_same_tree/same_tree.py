"""
Problem #: 100
Title:  Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true



Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false



Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

"""


# Definition for a binary tree node.
class TreeNode:

     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None):
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def get_test_case_1() -> (TreeNode, TreeNode):
    return None, None


def get_test_case_2() -> (TreeNode, TreeNode):
    return None, TreeNode(30)


def get_test_case_3() -> (TreeNode, TreeNode):
    return TreeNode(30), None


def get_test_case_4() -> (TreeNode, TreeNode):
    return TreeNode(30), TreeNode(10)


def get_test_case_5() -> (TreeNode, TreeNode):
    return TreeNode(30), TreeNode(30)


def get_test_case_6() -> (TreeNode, TreeNode):
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)

    one.left = two
    one.right = three

    return one, one


def get_test_case_7() -> (TreeNode, TreeNode):
    p_one = TreeNode(1)
    p_two = TreeNode(2)

    p_one.left = p_two

    q_one = TreeNode(1)
    q_two = TreeNode(2)

    q_one.right = q_two

    p = p_one
    q = q_one

    return p, q


def get_test_case_8() -> (TreeNode, TreeNode):
    p_node_1 = TreeNode(1)
    p_node_2 = TreeNode(2)
    p_node_3 = TreeNode(1)

    q_node_1 = TreeNode(1)
    q_node_2 = TreeNode(1)
    q_node_3 = TreeNode(2)

    p_node_1.left = p_node_2
    p_node_1.right = p_node_3

    q_node_1.left = q_node_2
    q_node_1.right = q_node_3

    p = p_node_1
    q = q_node_1

    return p, q


if __name__ == "__main__":
    solution = Solution()

    #p, q = get_test_case_1()
    #p, q = get_test_case_2()
    #p, q = get_test_case_3()
    #p, q = get_test_case_4()
    #p, q = get_test_case_5()
    #p, q = get_test_case_6()
    #p, q = get_test_case_7()
    p, q = get_test_case_7()

    identical = solution.isSameTree(p, q)
    print("\n identical: ", identical)
