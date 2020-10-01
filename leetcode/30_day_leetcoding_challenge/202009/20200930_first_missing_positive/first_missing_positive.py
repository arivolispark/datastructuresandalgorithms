"""
Title:  First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.



Example 1:
Input: [1,2,0]
Output: 3



Example 2:
Input: [3,4,-1,1]
Output: 2



Example 3:
Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

"""


from typing import List


class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums:
            numbers = set()

            for i in range(len(nums)):
                numbers.add(nums[i])

            i = 1
            while True:
                if i not in numbers:
                    return i
                else:
                    i += 1
        else:
            return 1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.firstMissingPositive([]), 1)
    test(solution.firstMissingPositive([1,2,0]), 3)
    test(solution.firstMissingPositive([3,4,-1,1]), 2)
    test(solution.firstMissingPositive([7,8,9,11,12]), 1)
