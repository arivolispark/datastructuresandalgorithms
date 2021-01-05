"""
Title:  Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]



Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

1) The number of nodes in the list is in the range [0, 300].
2) -100 <= Node.val <= 100
3) The list is guaranteed to be sorted in ascending order.

"""

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        list_1 = get_distinct_nodes(head)

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


def get_distinct_nodes(l1: ListNode) -> List[int]:
    result = list()
    val_freq_map = {}

    while l1:
        val_freq_map[l1.val] = val_freq_map.get(l1.val, 0) + 1
        l1 = l1.next

    for k, v in val_freq_map.items():
        if v == 1:
            result.append(k)

    result.sort()
    return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input():
    """
    [1,2,3,3,4,4,5]
    """

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(3)
    node_5 = ListNode(4)
    node_6 = ListNode(4)
    node_7 = ListNode(5)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = node_7

    head = node_1

    return head


def get_test_case_1_output():
    """
    [1,2,5]
    """

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(5)

    node_1.next = node_2
    node_2.next = node_3

    head = node_1

    return head


def get_test_case_2_input():
    """
    [1,1,1,2,3]
    """

    node_1 = ListNode(1)
    node_2 = ListNode(1)
    node_3 = ListNode(1)
    node_4 = ListNode(2)
    node_5 = ListNode(3)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    head = node_1

    return head


def get_test_case_2_output():
    """
    [2,3]
    """

    node_1 = ListNode(2)
    node_2 = ListNode(3)

    node_1.next = node_2

    head = node_1

    return head


if __name__ == "__main__":
    solution = Solution()

    test(get_list(solution.deleteDuplicates(get_test_case_1_input())), get_list(get_test_case_1_output()))
    test(get_list(solution.deleteDuplicates(get_test_case_2_input())), get_list(get_test_case_2_output()))
