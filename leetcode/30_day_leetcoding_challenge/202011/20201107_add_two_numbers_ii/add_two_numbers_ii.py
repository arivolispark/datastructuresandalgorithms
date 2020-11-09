"""
Title:  Add Two Number II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first 
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""

class ListNode:
 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_l1 = []
        stack_l2 = []

        while l1:
            stack_l1.append(l1)
            l1 = l1.next

        while l2:
            stack_l2.append(l2)
            l2 = l2.next

        carry = 0
        head = None

        while stack_l1 or stack_l2:
            v1 = stack_l1.pop().val if stack_l1 else 0
            v2 = stack_l2.pop().val if stack_l2 else 0
            v = v1 + v2
            carry, v = divmod(v+carry, 10)
            temp = head
            head = ListNode(v)
            head.next = temp

        if carry:
            temp = head
            head = ListNode(carry)
            head.next = temp
        return head        


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

