"""
Title:  Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume
that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.



Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]



Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]


Constraints:

1) 0 <= n, m <= 200
2) 1 <= n + m <= 200
3) nums1.length == m + n
4) nums2.length == n
5) -10^9 <= nums1[i], nums2[i] <= 10^9

"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1

        nums1.sort()


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input():
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    return nums1, m, nums2, n


def get_test_case_2_input():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0

    return nums1, m, nums2, n


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        get_test_case_1_input(),
        get_test_case_2_input()
    ]

    test_case_outputs = [
        [1,2,2,3,5,6],
        [1]
    ]

    for i in range(len(test_case_inputs)):
        solution.merge(test_case_inputs[i][0], test_case_inputs[i][1], test_case_inputs[i][2], test_case_inputs[i][3])
        test(test_case_inputs[i][0], test_case_outputs[i])
