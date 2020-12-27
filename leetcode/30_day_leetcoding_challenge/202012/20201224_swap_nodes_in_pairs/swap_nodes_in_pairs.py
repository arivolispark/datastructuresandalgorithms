
"""
Title:  Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.



Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]



Example 2:
Input: head = []
Output: []



Example 3:
Input: head = [1]
Output: [1]


Constraints:

1) The number of nodes in the list is in the range [0, 100].
2) 0 <= Node.val <= 100

"""

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        temp = ListNode(0)
        temp.next = head
        current = temp

        while current.next and current.next.next:
            runner = current.next.next
            current.next.next = runner.next
            runner.next = current.next
            current.next = runner
            current = current.next.next

        return temp.next


def traverse_list(head: ListNode) -> List[int]:
    result = list()
    while head:
        result.append(head.val)
        head = head.next
    return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input():
    return None


def get_test_case_1_output():
    return None


def get_test_case_2_input():
    return ListNode(1)


def get_test_case_2_output():
    return ListNode(1)


def get_test_case_3_input():
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)

    one.next = two
    two.next = three
    three.next = four

    head = one
    return head


def get_test_case_3_output():
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)

    two.next = one
    one.next = four
    four.next = three

    head = two
    return head


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        get_test_case_1_input(),
        get_test_case_2_input(),
        get_test_case_3_input(),
    ]

    test_case_outputs = [
        get_test_case_1_output(),
        get_test_case_2_output(),
        get_test_case_3_output(),
    ]

    for i in range(len(test_case_inputs)):
        result_list = solution.swapPairs(test_case_inputs[i])
        actual = traverse_list(result_list)

        expected = traverse_list(test_case_outputs[i])

        test(actual, expected)

