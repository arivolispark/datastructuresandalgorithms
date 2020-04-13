"""
Problem #: 142
Title:  Linked List Cycle 2

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an
integer pos which represents the position (0-indexed) in the linked
list where tail connects to. If pos is -1, then there is no cycle
in the linked list.

Note: Do not modify the linked list.


Example 1:

  [3] --> [2] --> [0] --> [-4]
           ^                |
           |                |
            ----------------

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

  [1] --> [2]
   ^       |
   |       |
    -------

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

  [1]

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


Follow up:
Can you solve it without using extra space?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        if head:
            if has_cycle(head):
                cycle_length = get_cycle_length(head)
                if cycle_length > -1:
                    slow, fast = head, head
                    i = 0
                    while i < cycle_length:
                        fast = fast.next
                        i += 1
                    while slow != fast:
                        slow = slow.next
                        fast = fast.next
                    return slow
            else:
                return None


def get_cycle_length(head: ListNode) -> int:
    cycle_length = 0
    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        cycle_length += 1

        if slow == fast:
            return cycle_length
    return -1


def has_cycle(head: ListNode) -> bool:
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

    cycle_starting_node = solution.detectCycle(head)
    if cycle_starting_node:
        print("\n cycle_starting_node.val: ", cycle_starting_node.val)
    else:
        print("\n No cycle detected")
        print("\n\n Display linked list")
        display(head)
