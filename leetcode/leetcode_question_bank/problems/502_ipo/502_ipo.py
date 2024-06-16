"""
Title:  502. IPO

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares
to Venture Capital, LeetCode would like to work on some projects to increase its capital
before the IPO. Since it has limited resources, it can only finish at most k distinct projects
before the IPO. Help LeetCode design the best way to maximize its total capital after finishing
at most k distinct projects.


You are given n projects where the ith project has a pure profit profits[i] and a minimum capital
of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and
the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and
return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.



Example 1:
Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.


Example 2:
Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6


Constraints:
1) 1 <= k <= 105
2) 0 <= w <= 109
3) n == profits.length
4) n == capital.length
5) 1 <= n <= 105
6) 0 <= profits[i] <= 104
7) 0 <= capital[i] <= 109

"""


from typing import List
from collections import deque
import heapq

class Solution:

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        current = w

        q = deque(sorted(zip(profits, capital), key=lambda x: (x[1], -x[0])))
        h = []

        for _ in range(k):
            while len(q) > 0 and q[0][1] <= current:
                p, _ = q.popleft()
                heapq.heappush(h, -p)

            if len(h) == 0:
                break

            p = -heapq.heappop(h)
            current += p

        return current


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if _name_ == '_main_':
    solution = Solution()

    test(solution.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]), 4)
    test(solution.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]), 6)
