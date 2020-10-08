"""
Title:  Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.



Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL



Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

"""


from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        k = k % n
        if k == 0:
            return head

        p1, p2 = head, head
        for i in range(k):
            p2 = p2.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next

        output = p1.next
        p1.next = None
        p2.next = head

        return output


def get_test_case_1_input():
    """
    Input: 1->2->3->4->5->NULL, k = 2

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

    k = 2

    return node_1, k


def get_test_case_1_output():
    """
    Output: 4->5->1->2->3->NULL

    """

    node_1 = ListNode(4)
    node_2 = ListNode(5)
    node_3 = ListNode(1)
    node_4 = ListNode(2)
    node_5 = ListNode(3)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5

    return node_1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    """
    test_case_inputs = [
        get_test_case_1_input(),
    ]

    test_case_outputs = [
        get_test_case_1_output(),
    ]

    for i in range(len(test_case_inputs)):
        test(solution.rotateRight(test_case_inputs[i][0], test_case_inputs[i][1]), test_case_outputs[i])
    """

