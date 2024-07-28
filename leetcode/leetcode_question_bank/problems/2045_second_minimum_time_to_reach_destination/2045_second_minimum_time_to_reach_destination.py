"""
Title:  2045. Second Minimum Time to Reach Destination

A city is represented as a bi-directional connected graph with n vertices
where each vertex is labeled from 1 to n (inclusive). The edges in the graph
are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes
a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected
by at most one edge, and no vertex has an edge to itself. The time taken to traverse
any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice
versa every change minutes. All signals change at the same time. You can enter a vertex
at any time, but can leave a vertex only when the signal is green. You cannot wait at a
vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the
minimum value.

 - For example the second minimum value of [2, 3, 4] is 3, and the second minimum value
of [2, 2, 4] is 4.

Given n, edges, time, and change, return the second minimum time it will take to go from
vertex 1 to vertex n.


Notes:
1) You can go through any vertex any number of times, including 1 and n.
2) You can assume that when the journey starts, all signals have just turned green.


Example 1:
Input: n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
Output: 13
Explanation:
The figure on the left shows the given graph.
The blue path in the figure on the right is the minimum time path.
The time taken is:
- Start at 1, time elapsed=0
- 1 -> 4: 3 minutes, time elapsed=3
- 4 -> 5: 3 minutes, time elapsed=6
Hence the minimum time needed is 6 minutes.

The red path shows the path to get the second minimum time.
- Start at 1, time elapsed=0
- 1 -> 3: 3 minutes, time elapsed=3
- 3 -> 4: 3 minutes, time elapsed=6
- Wait at 4 for 4 minutes, time elapsed=10
- 4 -> 5: 3 minutes, time elapsed=13
Hence the second minimum time is 13 minutes.


Example 2:
Input: n = 2, edges = [[1,2]], time = 3, change = 2
Output: 11
Explanation:
The minimum time path is 1 -> 2 with time = 3 minutes.
The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.


Constraints:
1) 2 <= n <= 104
2) n - 1 <= edges.length <= min(2 * 104, n * (n - 1) / 2)
3) edges[i].length == 2
4) 1 <= ui, vi <= n
5) ui != vi
6) There are no duplicate edges.
7) Each vertex can be reached directly or indirectly from every other vertex.
8) 1 <= time, change <= 103

"""

from typing import List
from collections import *
from heapq import *


class Solution:

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        INF = 100 * 100 * 100 * 100

        adj_list = defaultdict(list)
        cycle = change * 2
        for u, v in edges:
            u -= 1
            v -= 1
            adj_list[u].append(v)
            adj_list[v].append(u)

        distances_1 = [INF] * n
        distances_2 = [INF] * n

        distances_1[0] = 0
        distances_2[0] = INF

        heap = []
        heappush(heap, (0, 0, 0))

        while len(heap) > 0:
            distance, node, index = heappop(heap)

            if index == 0 and distances_1[node] > distance:
                continue
            if index == 1 and distances_2[node] > distance:
                continue
            if index == 1 and node == n - 1:
                return distance

            if distance % cycle < change:
                new_distance = distance + time
            else:
                new_distance = ((distance + cycle - 1) // cycle) * cycle + time

            for v in adj_list[node]:
                if new_distance < distances_1[v]:
                    distances_2[v] = distances_1[v]
                    distances_1[v] = new_distance
                    heappush(heap, (new_distance, v, 0))
                elif new_distance > distances_1[v] and new_distance < distances_2[v]:
                    distances_2[v] = new_distance
                    heappush(heap, (new_distance, v, 1))

        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.secondMinimum(5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5), 13)
    test(solution.secondMinimum(2, [[1,2]], 3, 2), 11)
