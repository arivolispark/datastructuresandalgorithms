"""
Title:  Odd Even Linked List

Given a singly linked list, group all odd nodes together followed
by the even nodes. Please note here we are talking about the node
number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.


Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL


Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL


Note:
1) The relative order inside both the even and odd groups should remain as it was in the input.
2) The first node is considered odd, the second node even and so on ...

"""

from typing import List


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        odd, temp_odd, first_odd = head, head, head
        even, temp_even, first_even = head.next, head.next, head.next

        process_odd = True

        while True:
            if process_odd is True:
                if temp_odd is not None and temp_odd.next is not None:
                    temp_odd = temp_odd.next.next
                    if temp_odd is not None:
                        odd.next = temp_odd
                        odd = odd.next
                    else:
                        odd.next = first_even
                    process_odd = False
                else:
                    odd.next = first_even
                    break
            if process_odd is False:
                if temp_even is not None and temp_even.next is not None:
                    temp_even = temp_even.next.next
                    even.next = temp_even
                    even = even.next
                    process_odd = True
                else:
                    break
        return first_odd


def create_list(head: ListNode) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def get_test_case_1_input():
    """
    Input: 1->2->3->4->5->NULL
    :return:
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

    return node_1


def get_test_case_1_output():
    """
    Output: 1->3->5->2->4->NULL
    :return:
    """

    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(2)
    node_5 = ListNode(4)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    return node_1


def get_test_case_2_input():
    """
    Input: 2->1->3->5->6->4->7->NULL
    :return:
    """
    node_1 = ListNode(2)
    node_2 = ListNode(1)
    node_3 = ListNode(3)
    node_4 = ListNode(5)
    node_5 = ListNode(6)
    node_6 = ListNode(4)
    node_7 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7

    return node_1


def get_test_case_2_output():
    """
    Output: 2->3->6->7->1->5->4->NULL
    :return:
    """
    node_1 = ListNode(2)
    node_2 = ListNode(3)
    node_3 = ListNode(6)
    node_4 = ListNode(7)
    node_5 = ListNode(1)
    node_6 = ListNode(5)
    node_7 = ListNode(4)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7

    return node_1


def get_test_case_3_input():
    """
    Input: 2->1->3->5->6->4->NULL
    :return:
    """
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_6 = ListNode(6)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6

    return node_1


def get_test_case_3_output():
    """
    Output: 2->3->6->1->5->4->NULL
    :return:
    """
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(2)
    node_5 = ListNode(4)
    node_6 = ListNode(6)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6

    return node_1


def get_test_case_4_input():
    """
    Input: NULL
    :return:
    """
    return None


def get_test_case_4_output():
    """
    Output: NULL
    :return:
    """
    return None


def get_test_case_5_input():
    """
    Input: 1->NULL
    :return:
    """
    return ListNode(1)


def get_test_case_5_output():
    """
    Output: 1->NULL
    :return:
    """
    return ListNode(1)


def get_test_case_6_input():
    """
    Input: 1->2->NULL
    :return:
    """
    node_1 = ListNode(1)
    node_2 = ListNode(2)

    node_1.next = node_2

    return node_1


def get_test_case_6_output():
    """
    Output: 1->2->NULL
    :return:
    """
    node_1 = ListNode(1)
    node_2 = ListNode(2)

    node_1.next = node_2

    return node_1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(create_list(solution.oddEvenList(get_test_case_1_input())), create_list(get_test_case_1_output()))
    test(create_list(solution.oddEvenList(get_test_case_2_input())), create_list(get_test_case_2_output()))
    test(create_list(solution.oddEvenList(get_test_case_3_input())), create_list(get_test_case_3_output()))
    test(create_list(solution.oddEvenList(get_test_case_4_input())), create_list(get_test_case_4_output()))
    test(create_list(solution.oddEvenList(get_test_case_5_input())), create_list(get_test_case_5_output()))
    test(create_list(solution.oddEvenList(get_test_case_6_input())), create_list(get_test_case_6_output()))

