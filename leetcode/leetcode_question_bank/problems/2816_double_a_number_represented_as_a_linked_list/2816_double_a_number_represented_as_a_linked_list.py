"""
Title:  2816. Double a Number Represented as a Linked List

You are given the head of a non-empty linked list representing a non-negative integer
without leading zeroes.

Return the head of the linked list after doubling it.


Example 1:
Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.


Example 2:
Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.


Constraints:
1) The number of nodes in the list is in the range [1, 10^4]
2) 0 <= Node.val <= 9
3) The input is generated such that the list represents a number that does
not have leading zeros, except the number 0 itself.

"""

from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value = 0
        while head:
            value = value * 10 + head.val
            head = head.next

        value *= 2

        if value == 0:
            return ListNode(0)

        tail = None
        while value > 0:
            tail = ListNode(value % 10, tail)
            value //= 10
        return tail


def get_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_case_1_input() -> Optional[ListNode]:
    one = ListNode(1)
    eight = ListNode(8)
    nine = ListNode(9)

    one.next = eight
    eight.next = nine

    root = one
    return root


def test_case_1_output() -> Optional[ListNode]:
    three = ListNode(3)
    seven = ListNode(7)
    eight = ListNode(8)

    three.next = seven
    seven.next = eight

    root = three

    return root


def test_case_2_input() -> Optional[ListNode]:
    nine_one = ListNode(9)
    nine_two = ListNode(9)
    nine_three = ListNode(9)

    nine_one.next = nine_two
    nine_two.next = nine_three

    root = nine_one
    return root


def test_case_2_output() -> Optional[ListNode]:
    one = ListNode(1)
    nine_one = ListNode(9)
    nine_two = ListNode(9)
    eight = ListNode(8)

    one.next = nine_one
    nine_one.next = nine_two
    nine_two.next = eight

    root = one

    return root


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test_case_1_result_list = solution.doubleIt(test_case_1_input())
    test(get_list(test_case_1_result_list), get_list(test_case_1_output()))

    test_case_2_result_list = solution.doubleIt(test_case_2_input())
    test(get_list(test_case_2_result_list), get_list(test_case_2_output()))
