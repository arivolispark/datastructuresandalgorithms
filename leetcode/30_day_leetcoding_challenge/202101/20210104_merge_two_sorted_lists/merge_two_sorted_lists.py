"""
Title:  Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.



Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]



Example 2:

Input: l1 = [], l2 = []
Output: []



Example 3:

Input: l1 = [], l2 = [0]
Output: [0]


Constraints:

1) The number of nodes in both lists is in the range [0, 50].
2) -100 <= Node.val <= 100
3) Both l1 and l2 are sorted in non-decreasing order.

"""

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None

        list_1 = get_list(l1)

        list_2 = get_list(l2)

        list_1.extend(list_2)

        list_1.sort()

        n = len(list_1)
        if n == 0:
            return None
        elif n == 1:
            return ListNode(list_1[0])

        head = ListNode(list_1[0])
        result = head

        for i in range(1, n):
            temp = ListNode(list_1[i])
            head.next = temp
            head = head.next

        return result


def get_list(l1: ListNode) -> List[int]:
    result = list()
    while l1:
        result.append(l1.val)
        l1 = l1.next
    return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input():
    l1_node_1 = ListNode(1)
    l1_node_2 = ListNode(2)
    l1_node_3 = ListNode(4)

    l1_node_1.next = l1_node_2
    l1_node_2.next = l1_node_3

    l1 = l1_node_1

    l2_node_1 = ListNode(1)
    l2_node_2 = ListNode(3)
    l2_node_3 = ListNode(4)

    l2_node_1.next = l2_node_2
    l2_node_2.next = l2_node_3

    l2 = l2_node_1

    return l1, l2


def get_test_case_1_output():
    l1_node_1 = ListNode(1)
    l1_node_2 = ListNode(1)
    l1_node_3 = ListNode(2)
    l1_node_4 = ListNode(3)
    l1_node_5 = ListNode(4)
    l1_node_6 = ListNode(4)

    l1_node_1.next = l1_node_2
    l1_node_2.next = l1_node_3
    l1_node_3.next = l1_node_4
    l1_node_4.next = l1_node_5
    l1_node_5.next = l1_node_6

    head = l1_node_1

    return head


def get_test_case_2_input():
    return None, None


def get_test_case_2_output():
    return None


def get_test_case_3_input():
    return None, ListNode(0)


def get_test_case_3_output():
    return ListNode(0)


if __name__ == "__main__":
    solution = Solution()

    test(get_list(solution.mergeTwoLists(get_test_case_1_input()[0], get_test_case_1_input()[1])), get_list(get_test_case_1_output()))
    test(get_list(solution.mergeTwoLists(get_test_case_2_input()[0], get_test_case_2_input()[1])), get_list(get_test_case_2_output()))
    test(get_list(solution.mergeTwoLists(get_test_case_3_input()[0], get_test_case_3_input()[1])), get_list(get_test_case_3_output()))
