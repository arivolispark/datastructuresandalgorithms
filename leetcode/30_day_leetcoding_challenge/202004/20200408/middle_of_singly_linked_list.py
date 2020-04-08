"""
Title:  Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.


Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

Note:
The number of nodes in the given list will be between 1 and 100.


Time:  O(N)
Space:  O(1)
"""


class ListNode:

     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:

    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


def traverse_singly_linked_list(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next


def get_lengh(head: ListNode) -> int:
    count = 0
    while head:
        head = head.next
        count += 1
    return count


def construct_empty_singly_linked_list() -> None:
    return None


def construct_singly_linked_list_with_one_node() -> ListNode:
    return ListNode(1)


def construct_singly_linked_list_with_odd_number_of_nodes() -> ListNode:
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


def construct_singly_linked_list_with_even_number_of_nodes() -> ListNode:
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

    return one


def display(head: ListNode) -> None:
    print("\n\n ==>> Display input singly_linked_list")
    traverse_singly_linked_list(head)

    length = get_lengh(head)
    print("\n length: ", length)

    middle_node = solution.middleNode(head)
    print("\n Display middle_node of the input singly_linked_list")
    traverse_singly_linked_list(middle_node)

    length = get_lengh(middle_node)
    print("\n length: ", length)


if __name__ == "__main__":
    solution = Solution()

    singly_linked_list_1 = construct_empty_singly_linked_list()
    display(singly_linked_list_1)

    singly_linked_list_2 = construct_singly_linked_list_with_one_node()
    display(singly_linked_list_2)

    singly_linked_list_3 = construct_singly_linked_list_with_odd_number_of_nodes()
    display(singly_linked_list_3)

    singly_linked_list_4 = construct_singly_linked_list_with_even_number_of_nodes()
    display(singly_linked_list_4)
