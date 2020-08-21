"""
Title:  Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.


Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.



Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

"""

from typing import List


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if head is None or head.next is None:
            return

        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        previous, current = None, slow

        while current is not None:
            tmp = current.next
            current.next = previous
            previous = current
            current = tmp

        n1, n2 = head, previous
        while n2.next is not None:
            tmp = n1.next
            n1.next = n2
            n1 = tmp

            tmp = n2.next
            n2.next = n1
            n2 = tmp


def display_list(head: ListNode) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def reverse(head: ListNode) -> None:
    if head is None or head.next is None:
        return

    predecessor, current, successor = head, head, head
    current = predecessor.next

    if current.next is None:
        current.next = predecessor
        predecessor.next = None
        return current


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input() -> ListNode:
    """
    Given 1->2->3->4, reorder it to 1->4->2->3.
    """

    return None


def get_test_case_2_input() -> ListNode:
    """
    Given 1, reorder it to 1.
    """

    node_1 = ListNode(1)
    head = node_1

    return head


def get_test_case_3_input() -> ListNode:
    """
    Given 1, reorder it to 1.
    """

    node_1 = ListNode(1)
    node_2 = ListNode(2)

    node_1.next = node_2

    head = node_1

    return head


def get_test_case_4_input() -> ListNode:
    """
    Given 1, reorder it to 1.
    """

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)

    node_1.next = node_2
    node_2.next = node_3

    head = node_1

    return head


def get_test_case_5_input() -> ListNode:
    """
    Given 1->2->3->4, reorder it to 1->4->2->3.
    """

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    head = node_1
    return head


def get_test_case_6_input() -> ListNode:
    """
    Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
    """

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


def get_test_case_1_output() -> List[int]:
    return None


def get_test_case_2_output() -> List[int]:
    return [1]


def get_test_case_3_output() -> List[int]:
    return [1, 2]


def get_test_case_4_output() -> List[int]:
    return [1, 2, 3]


def get_test_case_5_output() -> List[int]:
    return [1, 4, 2, 3]


def get_test_case_6_output() -> List[int]:
    return [1, 5, 2, 4, 3]


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        # get_test_case_1_input(),
        # get_test_case_2_input(),
        get_test_case_3_input(),
        # get_test_case_4_input(),
        # get_test_case_5_input(),
        # get_test_case_6_input(),
    ]

    test_case_outputs = [
        # get_test_case_1_output(),
        # get_test_case_2_output(),
        get_test_case_3_output(),
        # get_test_case_4_output(),
        # get_test_case_5_output(),
        # get_test_case_6_output(),
    ]

    for i in range(len(test_case_inputs)):
        head = test_case_inputs[i]
        solution.reorderList(head)

        test((display_list(head)), test_case_outputs[i])
