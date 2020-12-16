
"""
Title:  Plus One Linked List 

Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.



Example 1:
Input: head = [1,2,3]
Output: [1,2,4]



Example 2:
Input: head = [0]
Output: [1]
 

Constraints:

1) The number of nodes in the linked list is in the range [1, 100].
2) 0 <= Node.val <= 9
3) The number represented by the linked list does not contain leading zeros except for the zero itself. 

"""

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        head = reverseList(head)
        k = head
        carry = 0
        prev = None
        head.val += 1
 
        while (head != None) and (head.val > 9 or carry > 0):
            prev = head
            head.val += carry
            carry = head.val // 10
            head.val = head.val % 10
            head = head.next
 
        if carry > 0:
            prev.next = ListNode(carry)
        return reverseList(k)        


def reverseList(head):
    if not head:
        return
    curNode = head
    prevNode = head
    nextNode = head.next
    curNode.next = None
 
    while (nextNode):
        curNode = nextNode
        nextNode = nextNode.next
        curNode.next = prevNode
        prevNode = curNode
 
    return curNode


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()
