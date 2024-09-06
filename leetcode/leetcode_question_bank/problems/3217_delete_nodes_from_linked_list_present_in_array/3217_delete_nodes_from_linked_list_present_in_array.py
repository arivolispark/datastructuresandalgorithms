"""
Title:  3217. Delete Nodes From Linked List Present in Array

You are given an array of integers nums and the head of a linked list. Return the head of the
modified linked list after removing all nodes from the linked list that have a value that exists in nums.



Example 1:
Input: nums = [1,2,3], head = [1,2,3,4,5]
Output: [4,5]
Explanation:
Remove the nodes with values 1, 2, and 3.



Example 2:
Input: nums = [1], head = [1,2,1,2,1,2]
Output: [2,2,2]
Explanation:
Remove the nodes with value 1.



Example 3:
Input: nums = [5], head = [1,2,3,4]
Output: [1,2,3,4]
Explanation:
No node has value 5.



Constraints:
1) 1 <= nums.length <= 105
2) 1 <= nums[i] <= 105
3) All elements in nums are unique.
4) The number of nodes in the given list is in the range [1, 105].
5) 1 <= Node.val <= 105
The input is generated such that there is at least one node in the linked list that has a value not present in nums.

"""

from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        map = {}
        list_1 = []

        curr = head

        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1

        while curr:
            if curr.val not in map:
                list_1.append(curr.val)
            curr = curr.next

        if len(list_1) == 0:
            return None
        elif len(list_1) == 1:
            return ListNode(list_1[0])
        else:
            temp = ListNode(list_1[0])
            result = temp

            for i in range(1, len(list_1)):
                node = ListNode(list_1[i])
                temp.next = node
                temp = temp.next

        return result


def get_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def get_test_case_1_input() -> Optional[ListNode]:
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)

    one.next = two
    two.next = three
    three.next = four
    four.next = five

    return one


def get_test_case_1_output() -> Optional[ListNode]:
    four = ListNode(4)
    five = ListNode(5)

    four.next = five
  
    return four


def get_test_case_2_input() -> Optional[ListNode]:
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(1)
    four = ListNode(2)
    five = ListNode(1)
    six = ListNode(2)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six

    return one


def get_test_case_2_output() -> Optional[ListNode]:
    two = ListNode(2)
    four = ListNode(2)
    six = ListNode(2)

    two.next = four
    four.next = six

    return two


def get_test_case_3_input() -> Optional[ListNode]:
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)

    one.next = two
    two.next = three
    three.next = four

    return one


def get_test_case_3_output() -> Optional[ListNode]:
    return get_test_case_3_input()


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    li_1 = get_list(get_test_case_1_input())
    lo_1 = get_list(get_test_case_1_output())

    li_2 = get_list(get_test_case_2_input())
    lo_2 = get_list(get_test_case_2_output())
    li_3 = get_list(get_test_case_3_input())
    lo_3 = get_list(get_test_case_3_input())

    o1 = solution.modifiedList([1,2,3], get_test_case_1_input())
    o2 = solution.modifiedList([1], get_test_case_2_input())
    o3 = solution.modifiedList([5], get_test_case_3_input())


    test(get_list(o1), lo_1)
    test(get_list(o2), lo_2)
    test(get_list(o3), lo_3)
