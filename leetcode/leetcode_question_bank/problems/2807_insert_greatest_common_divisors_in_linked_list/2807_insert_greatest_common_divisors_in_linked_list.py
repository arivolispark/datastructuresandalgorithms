"""
Title:  2807. Insert Greatest Common Divisors in Linked List

Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the
greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly
divides both numbers.



Example 1:
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked
list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.


Example 2:
Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked
list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.


Constraints:
1) The number of nodes in the list is in the range [1, 5000].
2) 1 <= Node.val <= 1000

"""

from typing import Optional
from typing import List
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            temp = ListNode(math.gcd(curr.val, curr.next.val), curr.next)
            curr.next = temp
            curr = temp.next
        return head


def get_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def get_test_case_1_input():
    eighteen = ListNode(18)
    six = ListNode(6)
    ten = ListNode(10)
    three = ListNode(3)

    eighteen.next = six
    six.next = ten
    ten.next = three
    return eighteen


def get_test_case_1_output():
    eighteen = ListNode(18)
    six = ListNode(6)
    ten = ListNode(10)
    three = ListNode(3)
    six_1 = ListNode(6)
    two = ListNode(2)
    one = ListNode(1)

    eighteen.next = six_1
    six_1.next = six
    six.next = two
    two.next = ten
    ten.next = one
    one.next = three
    return eighteen


def get_test_case_2_input():
    return ListNode(7)


def get_test_case_2_output():
    return get_test_case_2_input()


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(get_list(solution.insertGreatestCommonDivisors(get_test_case_1_input())), get_list(get_test_case_1_output()))
    test(get_list(solution.insertGreatestCommonDivisors(get_test_case_2_input())), get_list(get_test_case_2_output()))
