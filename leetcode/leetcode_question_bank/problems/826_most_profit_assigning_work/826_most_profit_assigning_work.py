"""
Title:  826. Most Profit Assigning Work

You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a
job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total
profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.



Example 1:
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.


Example 2:
Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0


Constraints:
1) n == difficulty.length
2) n == profit.length
3) m == worker.length
4) 1 <= n, m <= 104
5) 1 <= difficulty[i], profit[i], worker[i] <= 105

"""

from typing import List
from collections import *


class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_profit = 0

        worker.sort()

        difficulty_profit = namedtuple('Difficulty_Profit', ['difficulty', 'profit'])
        difficulty_profit_queue = deque(sorted(list(difficulty_profit(d, p) for d, p in zip(difficulty, profit)), key=lambda d_p: d_p[0]))

        current_profit = 0
        for w in worker:
            while len(difficulty_profit_queue) > 0 and difficulty_profit_queue[0].difficulty <= w:
                d_p = difficulty_profit_queue.popleft()
                current_profit = max(current_profit, d_p.profit)

            max_profit += current_profit

        return max_profit


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if _name_ == '_main_':
    solution = Solution()

    test(solution.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]), 100)
    test(solution.maxProfitAssignment([85,47,57], [24,66,99], [40,25,25]), 0)
