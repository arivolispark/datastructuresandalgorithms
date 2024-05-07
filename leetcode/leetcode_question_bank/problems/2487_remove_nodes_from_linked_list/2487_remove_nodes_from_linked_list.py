# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d_list = deque()
        nums = []

        while head:
            if len(d_list) == 0:
                d_list.append(head.val)
            else:
                if head.val <= d_list[-1]:
                    d_list.append(head.val)
                else:
                    while len(d_list) > 0 and d_list[-1] < head.val:
                        d_list.pop()
                    d_list.append(head.val)
            head = head.next

        for i in range(len(d_list)):
            nums.append(d_list.pop())

        return insert_at_beginning(None, nums)


def insert_at_beginning(head: Optional[ListNode], nums: List[int]) -> Optional[ListNode]:
    if head:
        root = head
        for i in range(len(nums)):
            curr = ListNode(nums[i])
            curr.next = root
            root = curr
            return root
    else:
        root = head
        curr = ListNode(nums[0])
        curr.next = root
        root = curr

        for i in range(1, len(nums)):
            curr = ListNode(nums[i])
            curr.next = root
            root = curr
        return root
