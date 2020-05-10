"""
Title:  Valid Perfect Square

Given a positive integer num, write a function which returns True
if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true


Example 2:
Input: 14
Output: false

"""

from typing import List


class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        if -1 < num < 2:
            return True

        start = 2
        end = num // 2

        while start <= end:
            mid = start + (end - start) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def find_index(self, nums: List[int], key: int) -> int:
        if nums:
            start, end = 0, len(nums) - 1

            while start <= end:
                mid = start + (end - start) // 2

                if nums[mid] == key:
                    return mid
                elif nums[mid] < key:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    print("\n\n ==>> find_index")
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0), 0)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1), 1)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2), 2)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3), 3)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4), 4)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5), 5)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6), 6)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7), 7)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8), 8)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 9)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -10), -1)
    test(solution.find_index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 50), -1)

    print("\n\n ==>> isPerfectSquare")
    test(solution.isPerfectSquare(0), True)
    test(solution.isPerfectSquare(1), True)
    test(solution.isPerfectSquare(2), False)
    test(solution.isPerfectSquare(3), False)
    test(solution.isPerfectSquare(4), True)
    test(solution.isPerfectSquare(5), False)
    test(solution.isPerfectSquare(6), False)
    test(solution.isPerfectSquare(7), False)
    test(solution.isPerfectSquare(8), False)
    test(solution.isPerfectSquare(9), True)
    test(solution.isPerfectSquare(10), False)
    test(solution.isPerfectSquare(11), False)
    test(solution.isPerfectSquare(12), False)
    test(solution.isPerfectSquare(13), False)
    test(solution.isPerfectSquare(14), False)
    test(solution.isPerfectSquare(15), False)
    test(solution.isPerfectSquare(16), True)
    test(solution.isPerfectSquare(17), False)
    test(solution.isPerfectSquare(18), False)
    test(solution.isPerfectSquare(19), False)
    test(solution.isPerfectSquare(20), False)
    test(solution.isPerfectSquare(21), False)
    test(solution.isPerfectSquare(22), False)
    test(solution.isPerfectSquare(23), False)
    test(solution.isPerfectSquare(24), False)
    test(solution.isPerfectSquare(25), True)
    test(solution.isPerfectSquare(26), False)
    test(solution.isPerfectSquare(27), False)
    test(solution.isPerfectSquare(28), False)
    test(solution.isPerfectSquare(29), False)
    test(solution.isPerfectSquare(30), False)
    test(solution.isPerfectSquare(36), True)
    test(solution.isPerfectSquare(49), True)
    test(solution.isPerfectSquare(64), True)
    test(solution.isPerfectSquare(81), True)
    test(solution.isPerfectSquare(100), True)
    test(solution.isPerfectSquare(121), True)
    test(solution.isPerfectSquare(144), True)
    test(solution.isPerfectSquare(169), True)
    test(solution.isPerfectSquare(196), True)
    test(solution.isPerfectSquare(225), True)
    test(solution.isPerfectSquare(256), True)
    test(solution.isPerfectSquare(289), True)
    test(solution.isPerfectSquare(324), True)
    test(solution.isPerfectSquare(361), True)
    test(solution.isPerfectSquare(400), True)
    test(solution.isPerfectSquare(441), True)
    test(solution.isPerfectSquare(484), True)
    test(solution.isPerfectSquare(529), True)
    test(solution.isPerfectSquare(576), True)
    test(solution.isPerfectSquare(625), True)
    test(solution.isPerfectSquare(676), True)
    test(solution.isPerfectSquare(729), True)
    test(solution.isPerfectSquare(784), True)
    test(solution.isPerfectSquare(841), True)
    test(solution.isPerfectSquare(900), True)
