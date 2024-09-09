# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        result = [[-1] * n for _ in range(m)]
        x = 0
        y = 0
        d = 0

        curr = head
        while curr:
            result[x][y] = curr.val
            if (x + dirs[d][0] < 0 or x + dirs[d][0] == m or y + dirs[d][1] < 0 or
                    y + dirs[d][1] == n or result[x + dirs[d][0]][y + dirs[d][1]] != -1):
                d = (d + 1) % 4
            x += dirs[d][0]
            y += dirs[d][1]
            curr = curr.next

        return result
