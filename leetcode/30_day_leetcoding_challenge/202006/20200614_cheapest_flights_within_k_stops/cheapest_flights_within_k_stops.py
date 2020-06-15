"""
Title:  Cheapest Flights Within K Stops

There are n cities connected by m flights. Each flight starts
from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting
city src and the destination dst, your task is to find the
cheapest price from src to dst with up to k stops. If there
is no such route, output -1.


Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as
marked red in the picture.



Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as
marked blue in the picture.


Constraints:

1) The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
2) The size of flights will be in range [0, n * (n - 1) / 2].
3) The format of each flight will be (src, dst, price).
4) The price of each flight will be in the range [1, 10000].
5) k is in the range of [0, n - 1].
6) There will not be any duplicated flights or self cycles.

"""

from typing import List
import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0

        location = collections.defaultdict(list)
        prices = collections.defaultdict(lambda: float('inf'))

        for u, v, p in flights:
            location[u] += [(v, p)]

        q = [(src, -1, 0)]

        while q:
            position, k, cost = q.pop(0)
            if position == dst or k == K:
                continue
            for neighbor, p in location[position]:
                if cost + p >= prices[neighbor]:
                    continue
                else:
                    prices[neighbor] = cost + p
                    q += [(neighbor, k + 1, cost + p)]

        if prices[dst] < float('inf'):
            return prices[dst]
        else:
            return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1), 200)
    test(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0), 500)
    test(solution.findCheapestPrice(5, [[4, 1, 1], [1, 2, 3], [0, 3, 2], [0, 4, 10], [3, 1, 1], [1, 4, 3]], 2, 1, 1), -1)
