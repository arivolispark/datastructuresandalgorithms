"""
Problem #: 141
Title:  Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which
represents the position (0-indexed) in the linked list where tail
connects to. If pos is -1, then there is no cycle in the linked list.


Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""


# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        return False


def display(head: ListNode) -> None:
    while head:
        print(head.val, end=" ")
        head = head.next


def get_linked_list_test_case_1() -> ListNode:
    three = ListNode(3)
    two = ListNode(2)
    zero = ListNode(0)
    minus_four = ListNode(-4)

    three.next = two
    two.next = zero
    zero.next = minus_four
    minus_four.next = two

    head = three

    return head


def get_linked_list_test_case_2() -> ListNode:
    one = ListNode(1)
    two = ListNode(2)

    one.next = two
    two.next = one

    head = one

    return head


def get_linked_list_test_case_3() -> ListNode:
    one = ListNode(1)

    head = one

    return head


def get_linked_list_test_case_4() -> ListNode:
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    six = ListNode(6)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six

    head = one

    return head


if __name__ == "__main__":
    solution = Solution()

    #head = get_linked_list_test_case_1()
    #head = get_linked_list_test_case_2()
    #head = get_linked_list_test_case_3()
    head = get_linked_list_test_case_4()


    cycle = solution.hasCycle(head)
    print("\n cycle: ", cycle)
    if not cycle:
        print("\n\n Display linked list")
        display(head)
