"""
Title:  1497. Check If Array Pairs Are Divisible by k

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the
sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.



Example 1:
Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).


Example 2:
Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).


Example 3:
Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way
to divide arr into 3 pairs each with sum divisible by 10.


Constraints:
1) arr.length == n
2) 1 <= n <= 10^5
3) n is even.
4) -10^9 <= arr[i] <= 10^9
5) 1 <= k <= 10^5

"""

from typing import List


class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        count = [0] * k

        for a in arr:
            a %= k
            if a >= 0:
                count[a] += 1
            else:
                count[a + k] += 1

        return (count[0] % 2 == 0 and
                all(count[i] == count[k - i]
                    for i in range(1, k // 2 + 1)))


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.canArrange([1,2,3,4,5,10,6,7,8,9], 5), True)
    test(solution.canArrange([1,2,3,4,5,6], 7), True)
    test(solution.canArrange([1,2,3,4,5,6], 10), False)
