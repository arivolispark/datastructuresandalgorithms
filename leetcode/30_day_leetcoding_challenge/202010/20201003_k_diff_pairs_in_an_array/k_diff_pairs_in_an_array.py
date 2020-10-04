"""
Title:  K-diff Pairs in an Array

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
1) 0 <= i, j < nums.length
2) i != j
3) a <= b
4) b - a == k



Example 1:
Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.



Example 2:
Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).



Example 3:
Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).



Example 4:
Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2



Example 5:
Input: nums = [-1,-2,-3], k = 1
Output: 2



Constraints:
1) 1 <= nums.length <= 104
2) -10 ^ 7 <= nums[i] <= 10 ^ 7
3) 0 <= k <= 107

"""


from typing import List


class Solution:

    def findPairs(self, nums: List[int], k: int) -> int:
        result = set()
        if nums:
            nums.sort()
            for i in range(len(nums)):
                j = i + 1
                while j < len(nums) and abs(nums[j] - nums[i]) <= k:
                    if abs(nums[j] - nums[i] == k):
                        result.add((nums[i], nums[j]))
                    j += 1
        return len(result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findPairs([3,1,4,1,5], 2), 2)
    test(solution.findPairs([1,2,3,4,5], 1), 4)
    test(solution.findPairs([1,3,1,5,4], 0), 1)
    test(solution.findPairs([1,2,4,4,3,3,0,9,2,3], 3), 2)
    test(solution.findPairs([-1,-2,-3], 1), 2)
