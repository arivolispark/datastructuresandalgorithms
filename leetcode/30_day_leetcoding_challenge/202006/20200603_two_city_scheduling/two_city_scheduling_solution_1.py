"""
Title:  Two City Scheduling

There are 2N people a company is planning to interview. The cost of
flying the i-th person to city A is costs[i][0], and the cost of
flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that
exactly N people arrive in each city.


Example 1:
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have
half the people interviewing in each city.


Note:
1) 1 <= costs.length <= 100
2) It is guaranteed that costs.length is even.
3) 1 <= costs[i][0], costs[i][1] <= 1000

"""

from typing import List
from heapq import *


class Solution:

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = 0
        max_heap = []

        if costs:
            size = len(costs)
            for i in range(size):
                abs_diff = abs(costs[i][0] - costs[i][1])
                heappush(max_heap, (-abs_diff, costs[i]))

            city_a_count, city_b_count = 0, 0

            while max_heap:
                abs_diff, schedule = heappop(max_heap)
                if (city_a_count < size / 2) and (city_b_count < size / 2):
                    if schedule[0] < schedule[1]:
                        cost += schedule[0]
                        city_a_count += 1
                    else:
                        cost += schedule[1]
                        city_b_count += 1
                elif city_a_count < size / 2:
                    cost += schedule[0]
                    city_a_count += 1
                elif city_b_count < size / 2:
                    cost += schedule[1]
                    city_a_count += 1
                elif city_a_count == city_b_count == size / 2:
                    break
        return cost


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]), 110)
    test(solution.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]), 1859)
