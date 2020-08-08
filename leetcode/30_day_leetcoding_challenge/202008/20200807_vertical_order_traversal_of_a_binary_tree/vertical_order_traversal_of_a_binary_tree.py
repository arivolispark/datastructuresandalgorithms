"""
Title:  Vertical Order Traversal of a Binary Tree

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively
will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical
line touches some nodes, we report the values of the nodes in order from top to
bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported
first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will
have a list of values of nodes.



Example 1:

                3
              /   \
            9      20
                 /   \
                15    7


Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).



Example 2:

                1
              /   \
            2      3
           / \    /  \
         4    5  6    7


Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.


Note:
1) The tree will have between 1 and 1000 nodes.
2) Each node's value will be between 0 and 1000.


"""

from typing import List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        vertical_order_map = {}
        self.min_c, self_max_c = 0, 0

        def dfs(node, r, c):
            if node is None:
                return
            if c in vertical_order_map:
                vertical_order_map[c].append([r, node.val])
            else:
                vertical_order_map[c] = [[r, node.val]]

            self.min_c = min(self.min_c, c)
            self.max_c = max(self.max_c, c)
            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)

        dfs(root, 0, 0)
        for c in range(self.min_c, self.max_c + 1):
            col = sorted(vertical_order_map[c], key = lambda x: (x[0], x[1]))
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            result.append(col_sorted)

        return result


    def verticalTraversal_1(self, root: TreeNode) -> List[List[int]]:
        result = []

        vertical_order_node_list = []
        inorder_traversal(root, vertical_order_node_list, 0, 0)

        vertical_order_map = {}
        vertical_order_list = []

        for i in range(len(vertical_order_node_list)):
            node = vertical_order_node_list[i][0]
            y = vertical_order_node_list[i][1]

            if y not in vertical_order_list:
                vertical_order_list.append(y)

            if y not in vertical_order_map:
                vertical_order_map[y] = [node]
            else:
                l = vertical_order_map[y]
                l.append(node)

        #print(" vertical_order_map: ", vertical_order_map)
        #print(" vertical_order_list: ", vertical_order_list)

        for i in range(len(vertical_order_list)):
            l = vertical_order_map.get(vertical_order_list[i])
            l.sort()
            result.append(l)
        return result

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = []
        vertical_order_traversal_map = {}
        vertical_order_node_list = []

        printVertical(root, 0, vertical_order_traversal_map)

        # traverse the dictionary and print vertical nodes
        #print(" vertical_order_traversal_map: ", vertical_order_traversal_map)
        #for value in vertical_order_traversal_map.values():
        #    print(value)

        for key in vertical_order_traversal_map.keys():
            vertical_order_node_list.append(key)
        vertical_order_node_list.sort()
        #print(" vertical_order_node_list: ", vertical_order_node_list)

        for i in range(len(vertical_order_node_list)):
            #result.append(i)
            result.append(vertical_order_traversal_map.get(vertical_order_node_list[i]))
        return result


def printVertical(node, distance, vertical_order_traversal_map):
    if node is None:
        return

    # insert nodes present at current horizontal distance into the dict
    vertical_order_traversal_map.setdefault(distance, []).append(node.val)

    # recur for left subtree by decreasing horizontal distance by 1
    printVertical(node.left, distance - 1, vertical_order_traversal_map)

    # recur for right subtree by increasing horizontal distance by 1
    printVertical(node.right, distance + 1, vertical_order_traversal_map)


def inorder_traversal(root: TreeNode, result: List[int], x, y):
    if root is None:
        return
    inorder_traversal(root.left, result, x - 1, y - 1)
    result.append([root.val, x, y])
    inorder_traversal(root.right, result, x + 1, y - 1)


def get_test_case_1_input() -> TreeNode:
    """

                3
              /   \
            9      20
                 /   \
                15    7

    """

    node_1 = TreeNode(3)
    node_2 = TreeNode(9)
    node_3 = TreeNode(20)
    node_4 = TreeNode(15)
    node_5 = TreeNode(7)

    node_1.left = node_2
    node_1.right = node_3

    node_3.left = node_4
    node_3.right = node_5

    return node_1


def get_test_case_2_input() -> TreeNode:
    """

                1
              /   \
            2      3
           / \    /  \
         4    5  6    7

    """

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    return node_1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        get_test_case_1_input(),
        get_test_case_2_input(),
    ]

    test_case_outputs = [
        [[9],[3,15],[20],[7]],
        [[4],[2],[1,5,6],[3],[7]],
    ]

    for i in range(len(test_case_inputs)):
        test(solution.verticalTraversal(test_case_inputs[i]), test_case_outputs[i])
