"""
Title:  Pairs of Songs With Total Durations Divisible by 60

You are given a list of songs where the ith song has a duration
of time[i] seconds.

Return the number of pairs of songs for which their total duration
in seconds is divisible by 60. Formally, we want the number of
indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:
Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60



Example 2:
Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Constraints:

1) 1 <= time.length <= 6 * 10^4
2) 1 <= time[i] <= 500

"""

from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        from collections import Counter
        total = 0
        counts = Counter([x % 60 for x in time])

        if 30 in counts:
            total += counts[30] * (counts[30] - 1) / 2
            del counts[30]
        if 0 in counts:
            total += counts[0] * (counts[0] - 1) / 2
            del counts[0]

        for i in range(1, 30):
            if i in counts and (60 - i) in counts:
                total += counts[i] * counts[60 - i]

        return int(total)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.numPairsDivisibleBy60([30,20,150,100,40]), 3)
    test(solution.numPairsDivisibleBy60([60,60,60]), 3)
