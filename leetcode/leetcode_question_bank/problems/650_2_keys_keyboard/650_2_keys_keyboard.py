"""
Title:  650. 2 Keys Keyboard

There is only one character 'A' on the screen of a notepad. You can perform one
of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy
is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the
character 'A' exactly n times on the screen.



Example 1:
Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.


Example 2:
Input: n = 1
Output: 0


Constraints:
1) 1 <= n <= 1000

"""
from collections import deque


class Solution:

    def minSteps(self, n: int) -> int:
        result = {}
        q = deque()

        start = (1, 0)
        q.append(start)
        result[start] = 0

        while len(q) > 0:
            ch, buffer = q.popleft()
            move = result[(ch, buffer)]

            if ch == n:
                return move

            if (ch, ch) not in result:
                result[(ch, ch)] = move + 1
                q.append((ch,ch))

            if buffer > 0 and ch + buffer <= n and (ch + buffer, buffer) not in result:
                result[(ch + buffer), buffer] = move + 1
                q.append((ch + buffer, buffer))

        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.minSteps(3), 3)
    test(solution.minSteps(1), 0)
