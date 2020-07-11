"""
Title:  Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and
previous pointers, it could have a child pointer, which may or may not
point to a separate doubly linked list. These child lists may have one
or more children of their own, and so on, to produce a multilevel data
structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly
linked list. You are given the head of the first level of the list.



Example 1:
Input:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:

After flattening the multilevel linked list it becomes:



Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL



Example 3:
Input: head = []
Output: []

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL


The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]


To serialize all levels together we will add nulls in each level to
signify no node connects to the upper node of the previous level. The
serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]


Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]


Constraints:
1) Number of Nodes will not exceed 1000.
2) 1 <= Node.val <= 10^5


"""

from typing import List


class Node:

    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:

    def flatten(self, head: 'Node') -> 'Node':
        if head:
            self.helper(head)
        return head

    def helper(self, head):
        current, rear = head, head
        while current:
            child = current.child
            successor = current.next

            if child:
                _rear = self.helper(child)
                _rear.next = successor
                if successor:
                    successor.prev = _rear
                current.next = child
                child.prev = current
                current.child = None
                current = rear
            else:
                current = successor

            if current:
                rear = current

        return rear


def display(head: Node) -> List[int]:
    result = list()
    while head:
        result.append(head.val)
        head = head.next
    return result


def get_test_case_1() -> Node:
    return None


def get_test_case_2() -> Node:
    return Node(1, None, None, None)


def get_test_case_3() -> Node:
    """
           1
         /   \
        3     2
    """
    node_1 = Node(1, None, None, None)
    node_2 = Node(2, None, None, None)
    node_3 = Node(3, None, None, None)
    node_4 = Node(4, None, None, None)
    node_5 = Node(5, None, None, None)
    node_6 = Node(6, None, None, None)
    node_7 = Node(7, None, None, None)
    node_8 = Node(8, None, None, None)
    node_9 = Node(9, None, None, None)
    node_10 = Node(10, None, None, None)
    node_11 = Node(11, None, None, None)
    node_12 = Node(12, None, None, None)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6

    node_6.prev = node_5
    node_5.prev = node_4
    node_4.prev = node_3
    node_3.prev = node_2
    node_2.prev = node_1


    node_7.next = node_8
    node_8.next = node_9
    node_9.next = node_10

    node_10.prev = node_9
    node_9.prev = node_8
    node_8.prev = node_7


    node_11.next = node_12

    node_12.prev = node_11

    node_3.child = node_7

    node_8.child = node_11

    return node_1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    #test(solution.flatten(get_test_case_1()), None)
    #test(solution.flatten(get_test_case_2()), None)
    #test(solution.flatten(get_test_case_3()), None)

    node = solution.flatten(get_test_case_3())
    result = display(node)
    print(" result: ", result)
