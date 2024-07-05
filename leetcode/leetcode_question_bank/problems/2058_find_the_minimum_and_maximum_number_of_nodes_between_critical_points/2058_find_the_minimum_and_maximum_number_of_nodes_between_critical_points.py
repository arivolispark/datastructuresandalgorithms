"""
Title:  2058. Find the Minimum and Maximum Number of Nodes Between Critical Points

A critical point in a linked list is defined as either a local maxima
or a local minima.

A node is a local maxima if the current node has a value strictly greater
than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller
than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a
previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance]
where minDistance is the minimum distance between any two distinct critical points and
maxDistance is the maximum distance between any two distinct critical points. If there
are fewer than two critical points, return [-1, -1].



Example 1:
Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].


Example 2:
Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.


Example 3:
Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.


Constraints:
1) The number of nodes in the list is in the range [2, 10^5].
2) 1 <= Node.val <= 10^5

"""

from typing import List
from typing import Optional
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = []
        critical_point = []
        min_distance = math.inf

        index = 1
        previous = 0

        if head is None or head.next is None:
            return [-1, -1]

        curr = head
        previous = curr.val

        curr = curr.next
        index += 1

        while curr:
            if curr.next is not None:
                if previous > curr.val and curr.val < curr.next.val:
                    critical_point.append(index)
                elif previous < curr.val and curr.val > curr.next.val:
                    critical_point.append(index)
            previous = curr.val
            curr = curr.next
            index += 1

        if len(critical_point) < 2:
            return [-1, -1]

        for i in range(len(critical_point) - 1):
            min_distance = min(min_distance, abs(critical_point[i] - critical_point[i+1]))

        max_distance = abs(critical_point[0] - critical_point[-1])

        result.append(min_distance)
        result.append(max_distance)

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input():
    one = ListNode(3)
    two = ListNode(1)

    one.next = two

    return one


def get_test_case_2_input():
    # [5, 3, 1, 2, 5, 1, 2]

    one = ListNode(5)
    two = ListNode(3)
    three = ListNode(1)
    four = ListNode(2)
    five = ListNode(5)
    six = ListNode(1)
    seven = ListNode(2)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    six.next = seven

    return one


def get_test_case_3_input():
    # [1,3,2,2,3,2,2,2,7]

    one = ListNode(1)
    two = ListNode(3)
    three = ListNode(2)
    four = ListNode(2)
    five = ListNode(3)
    six = ListNode(2)
    seven = ListNode(2)
    eight = ListNode(2)
    nine = ListNode(7)

    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    six.next = seven
    seven.next = eight
    eight.next = nine

    return one


if __name__ == '__main__':
    solution = Solution()

    test(solution.nodesBetweenCriticalPoints(get_test_case_1_input()), [-1,-1])
    test(solution.nodesBetweenCriticalPoints(get_test_case_2_input()), [1,3])
    test(solution.nodesBetweenCriticalPoints(get_test_case_3_input()), [3,3])
