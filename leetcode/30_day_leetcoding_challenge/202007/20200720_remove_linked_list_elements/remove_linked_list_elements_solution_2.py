"""
Title:  Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.


Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""

from typing import List


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_list(head: ListNode) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def get_test_case_1_input() -> (ListNode, int):
    """
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
    """

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(6)
    node_4 = ListNode(3)
    node_5 = ListNode(4)
    node_6 = ListNode(5)
    node_7 = ListNode(6)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7

    head_1 = node_1

    return head_1, 6


def get_test_case_1_output() -> ListNode:
    """
    Output: 1->2->3->4->5
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

    head_1 = node_1

    return head_1


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        [get_test_case_1_input()[0], get_test_case_1_input()[1]],
    ]

    test_case_outputs = [
        [get_test_case_1_output()],
    ]

    for i in range(len(test_case_inputs)):
        solution.removeElements(test_case_inputs[i][0], test_case_inputs[i][1])
        test(get_list(test_case_inputs[i][0]), get_list(test_case_outputs[i][0]))
