"""
Title:  Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and
some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means
empty and 1 means not empty, and an integer n, return if n new flowers
can be planted in the flowerbed without violating the no-adjacent-flowers rule.



Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true



Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false



Constraints:

1) 1 <= flowerbed.length <= 2 * 10^4
2) flowerbed[i] is 0 or 1.
3) There are no two adjacent flowers in flowerbed.
4) 0 <= n <= flowerbed.length

"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        flowerbed = [0] + flowerbed + [0]
        flowerbed_len = len(flowerbed)

        for i in range(1, flowerbed_len - 1):
            if flowerbed[i]:
                continue
            elif flowerbed[i - 1] == flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
                if n == 0:
                    return True
        return False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.canPlaceFlowers([1,0,0,0,1], 1), True)
    test(solution.canPlaceFlowers([1,0,0,0,1], 2), False)
    test(solution.canPlaceFlowers([0,0,1,0,1], 1), True)
