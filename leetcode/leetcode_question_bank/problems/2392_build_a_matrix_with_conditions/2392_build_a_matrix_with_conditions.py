"""
Title:  2392. Build a Matrix With Conditions

You are given a positive integer k. You are also given:
1) a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
2) a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].

The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

1) The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
2) The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.

Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.



Example 1:
Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.

The row conditions are the following:
- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.

The column conditions are the following:
- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.


Example 2:
Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.


Constraints:
1) 2 <= k <= 400
2) 1 <= rowConditions.length, colConditions.length <= 10^4
3) rowConditions[i].length == colConditions[i].length == 2
4) 1 <= abovei, belowi, lefti, righti <= k
5) abovei != belowi
6) lefti != righti

"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions):
            dependency = defaultdict(list)
            in_degree = [0] * k
            for a, b in conditions:
                a -= 1
                b -= 1

                dependency[a].append(b)
                in_degree[a] += 0
                in_degree[b] += 1

            q = deque()

            for i in range(k):
                if in_degree[i] == 0:
                    q.append(i)

            ordering = []
            while len(q) > 0:
                current = q.popleft()
                ordering.append(current)

                for nxt in dependency[current]:
                    in_degree[nxt] -= 1

                    if in_degree[nxt] == 0:
                        q.append(nxt)

            assert(len(ordering) == k)
            return {x : i for i, x in enumerate(ordering)}

        result = [[0] * k for _ in range(k)]
        try:
            rows = topological_sort(rowConditions)
            cols = topological_sort(colConditions)
            for i in range(k):
                result[rows[i]][cols[i]] = i + 1
            return result
        except:
            return []


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]]), [[3,0,0],[0,0,1],[0,2,0]])
    test(solution.buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]), [])
