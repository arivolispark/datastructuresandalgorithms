"""
Title:  1482. Minimum Number of Days to Make m Bouquets

You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent
flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i]
and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets
from the garden. If it is impossible to make m bouquets return -1.



Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.


Example 2:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.


Example 3:
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.


Constraints:
1) bloomDay.length == n
2) 1 <= n <= 10^5
3) 1 <= bloomDay[i] <= 10^9
4) 1 <= m <= 10^6
5) 1 <= k <= n

"""


from typing import List


class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        length = len(bloomDay)

        if m * k > length:
            return -1

        parents = [x for x in range(length)]
        sz = [1] * length

        def ufind(x):
            if parents[x] != x:
                parents[x] = ufind(parents[x])
            return parents[x]

        def uunion(a, b):
            ua = ufind(a)
            ub = ufind(b)

            if ua != ub:
                parents[ua] = ub
                sz[ub] += sz[ua]

        events = []
        for index, x in enumerate(bloomDay):
            events.append((x, index))

        events.sort()

        count = 0
        bloomed = [False] * length
        for t, index in events:
            bloomed[index] = True

            if index - 1 >= 0 and bloomed[index - 1]:
                count -= sz[ufind(index - 1)] // k
                uunion(index, index - 1)
            if index + 1 < length and bloomed[index + 1]:
                count -= sz[ufind(index + 1)] // k
                uunion(index, index + 1)

            count += sz[ufind(index)] // k

            if count >= m:
                return t

        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.minDays([1,10,3,10,2],3, 1), 3)
    test(solution.minDays([1,10,3,10,2],3, 2), -1)
    test(solution.minDays([7,7,7,7,12,7,7],2, 3), 12)
