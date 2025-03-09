"""
Title:  2379. Minimum Recolors to Get K Consecutive Black Blocks

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing
the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive
black blocks.



Example 1:
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.


Example 2:
Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.



Constraints:
1) n == blocks.length
2) 1 <= n <= 100
3) blocks[i] is either 'W' or 'B'.
4) 1 <= k <= n

"""

from typing import List
import math


class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = math.inf
        length = len(blocks)

        for i in range(length - k + 1):
            window_sum = 0
            left = i

            for j in range(left, left + k):
                if blocks[j] == "B":
                    window_sum += 1

            if window_sum >= k:
                return 0
            else:
                result = min(result, k - window_sum)

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.minimumRecolors("WBBWWBBWBW", 7), 3)
    test(solution.minimumRecolors("WBWBBBW", 2), 0)
