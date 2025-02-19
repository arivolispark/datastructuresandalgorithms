"""
Title:  1415. The k-th Lexicographical String of All Happy Strings of Length n

A happy string is a string that:

1) consists only of letters of the set ['a', 'b', 'c'].
2) s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).


For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.



Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".


Example 2:
Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.


Example 3:
Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"


Constraints:
1) 1 <= n <= 10
2) 1 <= k <= 100

"""

from typing import List
from collections import deque


class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        nextLetters = {"a": "bc", "b": "ac", "c": "ab"}

        q = deque()

        q.append("a")
        q.append("b")
        q.append("c")

        while len(q[0]) != n:
            c = q.popleft()
            for nextLetter in nextLetters[c[-1]]:
                q.append(c + nextLetter)

        return "" if len(q) < k else q[k - 1]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.getHappyString(1, 3), "c")
    test(solution.getHappyString(1, 4), "")
    test(solution.getHappyString(3, 9), "cab")
