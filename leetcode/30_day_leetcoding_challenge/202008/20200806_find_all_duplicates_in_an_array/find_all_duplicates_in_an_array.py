"""
Title:  Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some
elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

"""

from typing import List


class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()
        if nums:
            nums.sort()
            #print(" nums: ", nums)
            for i in range(1, len(nums)):
                if nums[i - 1] == nums[i]:
                    result.add(nums[i - 1])
        return list(result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findDuplicates([4,3,2,7,8,2,3,1]), [2,3])
    test(solution.findDuplicates([4,3,2,7,8,2,3,1,2,3,4,4,4,5,7]), [2,3,4,7])
