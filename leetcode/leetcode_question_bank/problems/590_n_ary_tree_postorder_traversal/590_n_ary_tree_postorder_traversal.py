"""
Title:  590. N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group
of children is separated by the null value (See examples)



Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]


Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]


Constraints:
1) The number of nodes in the tree is in the range [0, 104^].
2) 0 <= Node.val <= 10^4
3) The height of the n-ary tree is less than or equal to 1000.


Follow up: Recursive solution is trivial, could you do it iteratively?

"""

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(root: Node):
            if root is None:
                return

            child_list = root.children
            if child_list:
                for n in child_list:
                    dfs(n)
            result.append(root.val)

        dfs(root)
        return result


def get_test_case_1_input():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    l1 = []
    l1.append(three)
    l1.append(two)
    l1.append(four)

    one.children = l1

    l2 = []
    l2.append(five)
    l2.append(six)

    three.children = l2
    return one


def get_test_case_2_input():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)

    thirteen = Node(13)
    fourteen = Node(14)

    l1 = []
    l1.append(two)
    l1.append(three)
    l1.append(four)
    l1.append(five)
    one.children = l1

    l2 = []
    l2.append(six)
    l2.append(seven)
    three.children = l2

    l3 = []
    l3.append(eleven)
    seven.children = l3

    l4 = []
    l4.append(fourteen)
    eleven.children = l4

    l5 = []
    l5.append(eight)
    four.children = l5

    l6 = []
    l6.append(twelve)
    eight.children = l6

    l7 = []
    l7.append(nine)
    l7.append(ten)
    five.children = l7

    l8 = []
    l8.append(thirteen)
    nine.children = l8

    return one


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.postorder(get_test_case_1_input()), [5,6,3,2,4,1])
    test(solution.postorder(get_test_case_2_input()), [2,6,14,11,7,3,12,8,4,13,9,10,5,1])
