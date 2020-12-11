"""
Title:  Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

1) arr.length >= 3
2) There exists some i with 0 < i < arr.length - 1 such that:
    a) arr[0] < arr[1] < ... < arr[i - 1] < A[i]
    b) arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


Mountain array:
0    2    3    4    5        2         1        0
<- Strictly increasing -> <- Strictly decreasing ->


Not a mountain array:
0      2      3      3      5        2        1        0
<- Increasing but not strictly -> <- Strictly decreasing ->


Example 1:
Input: arr = [2,1]
Output: false



Example 2:
Input: arr = [3,5,5]
Output: false



Example 3:
Input: arr = [0,3,2,1]
Output: true



Constraints:

1) 1 <= arr.length <= 10^4
2) 0 <= arr[i] <= 10^4

"""

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i, j, n = 0, len(arr) - 1, len(arr)
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        while j > 0 and arr[j - 1] > arr[j]:
            j -= 1
        return 0 < i == j < n - 1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.validMountainArray([]), False)
    test(solution.validMountainArray([2]), False)
    test(solution.validMountainArray([2,1]), False)
    test(solution.validMountainArray([1,3,2]), True)
    test(solution.validMountainArray([3,5,5]), False)
    test(solution.validMountainArray([0,3,2,1]), True)
    test(solution.validMountainArray([0,2,3,4,5,2,1,0]), True)
    test(solution.validMountainArray([0,2,3,3,5,2,1,0]), False)
    test(solution.validMountainArray([0,1,2,3,4,5,6,7,8,9]), False)
    test(solution.validMountainArray([9,8,7,6,5,4,3,2,1,0]), False)
    test(solution.validMountainArray([0,1,2,1,2]), False)
