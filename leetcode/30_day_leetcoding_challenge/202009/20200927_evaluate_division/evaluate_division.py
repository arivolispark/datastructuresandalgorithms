"""
Title:  Evaluate Division

You are given equations in the format A / B = k, where A and B are variables represented
as strings, and k is a real number (floating-point number). Given some queries, return
the answers. If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no
division by zero and there is no contradiction.



Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]



Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]



Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:
1) 1 <= equations.length <= 20
2) equations[i].length == 2
3) 1 <= equations[i][0], equations[i][1] <= 5
4) values.length == equations.length
5) 0.0 < values[i] <= 20.0
6) 1 <= queries.length <= 20
7) queries[i].length == 2
8) 1 <= queries[i][0], queries[i][1] <= 5
9) equations[i][0], equations[i][1], queries[i][0], queries[i][1] consist of lower case English letters and digits.

"""


from typing import List
import collections


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        table = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            table[x][y] = value
            table[y][x] = 1.0 / value
        answer = [self.dfs(x, y, table, set()) if x in table and y in table else -1.0 for (x, y) in queries]
        return answer

    def dfs(self, x, y, table, visited):
        if x == y:
            return 1.0
        visited.add(x)
        for n in table[x]:
            if n in visited:
                continue
            visited.add(n)
            d = self.dfs(n, y, table, visited)
            if d > 0:
                return d * table[x][n]
        return -1.0


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]), [6.00000,0.50000,-1.00000,1.00000,-1.00000])
    test(solution.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]), [3.75000,0.40000,5.00000,0.20000])
    test(solution.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]), [0.50000,2.00000,-1.00000,-1.00000])
