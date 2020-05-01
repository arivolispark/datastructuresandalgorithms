"""
Title:  Binary Tree Maximum Path Sum


Given a binary tree where each path going from the root to any
leaf form a valid sequence, check if a given string is a valid
sequence in such binary tree.

We get the given string from the concatenation of an array of
integers arr and the concatenation of all values of the nodes
along a path results in a sequence in the given binary tree.


Example 1:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true

Explanation:
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure).
Other valid sequences are:
0 -> 1 -> 1 -> 0
0 -> 0 -> 0



Example 2:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.



Example 3:

Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.


Constraints:
1) 1 <= arr.length <= 5000
2) 0 <= arr[i] <= 9
3) Each node's value is between [0 - 9].

"""


from typing import List
from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        size = len(arr)
        i = 0
        return validate_sequence(root, arr, size, i)


def validate_sequence(root, arr, size, i):
    if root is None:
        return size == 0

    if (i == size - 1) and (root.left is None and root.right is None) and (root.val == arr[i]):
        return True

    if (i < size) and (root.val == arr[i]):
        return validate_sequence(root.left, arr, size, i + 1) or validate_sequence(root.right, arr, size, i + 1)


def inorder_traversal(root: TreeNode) -> None:
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)


def level_order_traversal(root: TreeNode) -> List[int]:
    queue = deque()
    result = []
    if root is None:
        return result

    queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()
        print(node.val, end=" ")
        result.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
    return result


def get_test_case_1() -> (TreeNode, List[int]):
    node_1 = TreeNode(0)
    node_2 = TreeNode(1)
    node_3 = TreeNode(0)
    node_4 = TreeNode(1)
    node_5 = TreeNode(1)
    node_6 = TreeNode(0)
    node_7 = TreeNode(0)
    node_8 = TreeNode(0)
    node_9 = TreeNode(0)

    node_1.left = node_2
    node_2.left = node_3
    node_3.right = node_4

    node_2.right = node_5
    node_5.left = node_6
    node_5.right = node_7

    node_1.right = node_8
    node_8.left = node_9

    head = node_1

    arr = [0, 1, 0, 1]

    return head, arr


def get_test_case_2() -> (TreeNode, List[int]):
    node_1 = TreeNode(0)
    node_2 = TreeNode(1)
    node_3 = TreeNode(0)
    node_4 = TreeNode(1)
    node_5 = TreeNode(1)
    node_6 = TreeNode(0)
    node_7 = TreeNode(0)
    node_8 = TreeNode(0)
    node_9 = TreeNode(0)

    node_1.left = node_2
    node_2.left = node_3
    node_3.right = node_4

    node_2.right = node_5
    node_5.left = node_6
    node_5.right = node_7

    node_1.right = node_8
    node_8.left = node_9

    head = node_1

    arr = [0, 0, 1]

    return head, arr


def get_test_case_3() -> (TreeNode, List[int]):
    node_1 = TreeNode(0)
    node_2 = TreeNode(1)
    node_3 = TreeNode(0)
    node_4 = TreeNode(1)
    node_5 = TreeNode(1)
    node_6 = TreeNode(0)
    node_7 = TreeNode(0)
    node_8 = TreeNode(0)
    node_9 = TreeNode(0)

    node_1.left = node_2
    node_2.left = node_3
    node_3.right = node_4

    node_2.right = node_5
    node_5.left = node_6
    node_5.right = node_7

    node_1.right = node_8
    node_8.left = node_9

    head = node_1

    arr = [0, 1, 1]

    return head, arr


def get_test_case_4() -> (TreeNode, List[int]):
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_8 = TreeNode(8)
    node_9 = TreeNode(9)

    node_7.left = node_3
    node_7.right = node_9

    node_3.left = node_1
    node_3.right = node_5

    node_1.right = node_2

    node_5.left = node_4
    node_5.right = node_6

    node_9.left = node_8

    head = node_7

    arr = [7, 3, 1, 2]

    return head, arr


if __name__ == "__main__":
    solution = Solution()

    #root, arr = get_test_case_1()
    #root, arr = get_test_case_2()
    #root, arr = get_test_case_3()
    root, arr = get_test_case_4()

    print("\n\n Inorder traversal")
    inorder_traversal(root)

    print("\n\n Level order traversal")
    level_order_traversal_result = level_order_traversal(root)
    print("\n level_order_traversal_result: ", level_order_traversal_result)

    print("\n\n arr: ", arr)

    valid_flag = solution.isValidSequence(root, arr)
    print("\n valid_flag: ", valid_flag)
