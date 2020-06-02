"""
Title:  Delete Node in a Linked List


Write a function to delete a node (except the tail) in a
singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:


Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the
linked list should become 4 -> 1 -> 9 after calling your function.


Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


Note:
1) The linked list will have at least two elements.
2) All of the nodes' values will be unique.
3) The given node will not be the tail and it will always be a valid node of the linked list.
4) Do not return anything from your function.

"""


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteNode(self, node) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next


def display(head: ListNode) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next


def get_test_case_3_input() -> ListNode:
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    head = node_1

    return head


"""    
def get_test_case_3_output() -> TreeNode:
    node_1 = TreeNode(1)
    return node_1


def get_test_case_4_input() -> TreeNode:
    node_1 = TreeNode(1)
    node_2 = TreeNode(2)

    node_1.left = node_2

    return node_1
"""


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    print()
    head = get_test_case_3_input()
    display(head)

    print()
    solution.deleteNode(head)
    display(head)
