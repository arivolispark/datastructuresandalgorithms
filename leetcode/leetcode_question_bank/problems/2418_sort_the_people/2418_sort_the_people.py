"""
Title:  2418. Sort the People

You are given an array of strings names, and an array heights that consists of distinct
positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.



Example 1:
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.


Example 2:
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.


Constraints:
1) n == names.length == heights.length
2) 1 <= n <= 10^3
3) 1 <= names[i].length <= 20
4) 1 <= heights[i] <= 10^5
5) names[i] consists of lower and upper case English letters.
6) All the values of heights are distinct.

"""

from typing import List
from heapq import *


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result = []
        max_heap = []

        for i in range(len(heights)):
            heappush(max_heap, [-heights[i], names[i]])

        while max_heap:
            height, name = heappop(max_heap)
            result.append(name)

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.sortPeople(["Mary", "John", "Emma"], [180,165,170]), ["Mary", "Emma", "John"])
    test(solution.sortPeople(["Alice", "Bob", "Bob"], [155,185,150]), ["Bob", "Alice", "Bob"])
