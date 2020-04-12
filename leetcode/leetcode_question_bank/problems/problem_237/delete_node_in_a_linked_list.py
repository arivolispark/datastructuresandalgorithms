"""
Problem #: 237
Title:  Delete Node in a Linked List

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:


Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


Note:
    1) The linked list will have at least two elements.
    2) All of the nodes' values will be unique.
    3) The given node will not be the tail and it will always be a valid node of the linked list.
    4) Do not return anything from your function.
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        slow, fast = node, node
        if fast.next is not None:
            fast = fast.next

        while fast.next:
            slow.val = fast.val
            slow = slow.next
            fast = fast.next
        slow.val = fast.val
        slow.next = None


def display(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next


def get_linked_list_test_case_1():
    four = ListNode(4)
    five = ListNode(5)

    four.next = five

    head = four
    node_to_delete = four

    return head, node_to_delete


def get_linked_list_test_case_2():
    four = ListNode(4)
    five = ListNode(5)
    one = ListNode(1)

    four.next = five
    five.next = one

    head = four
    node_to_delete = four

    return head, node_to_delete


def get_linked_list_test_case_3():
    four = ListNode(4)
    five = ListNode(5)
    one = ListNode(1)
    nine = ListNode(9)

    four.next = five
    five.next = one
    one.next = nine

    head = four
    node_to_delete = four

    return head, node_to_delete


def get_linked_list_test_case_4():
    four = ListNode(4)
    five = ListNode(5)
    one = ListNode(1)
    nine = ListNode(9)

    four.next = five
    five.next = one
    one.next = nine

    head = four
    node_to_delete = five

    return head, node_to_delete


def get_linked_list_test_case_5():
    four = ListNode(4)
    five = ListNode(5)
    one = ListNode(1)
    nine = ListNode(9)

    four.next = five
    five.next = one
    one.next = nine

    head = four
    node_to_delete = one

    return head, node_to_delete


if __name__ == "__main__":
    solution = Solution()

    #head, node_to_delete = get_linked_list_test_case_1()
    #head, node_to_delete = get_linked_list_test_case_2()
    #head, node_to_delete = get_linked_list_test_case_3()
    head, node_to_delete = get_linked_list_test_case_4()
    #head, node_to_delete = get_linked_list_test_case_5()

    print("\n\n Display linked list")
    display(head)

    solution.deleteNode(node_to_delete)

    print("\n\n Display linked list")
    display(head)
