"""
Title:  Missing Ranges

You are given an inclusive range [lower, upper] and a sorted unique integer
array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is
not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly.
That is, no element of nums is in any of the ranges, and each missing number is in
one of the ranges.

Each range [a,b] in the list should be output as:
1) "a->b" if a != b
2) "a" if a == b



Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"



Example 2:
Input: nums = [], lower = 1, upper = 1
Output: ["1"]
Explanation: The only missing range is [1,1], which becomes "1".



Example 3:
Input: nums = [], lower = -3, upper = -1
Output: ["-3->-1"]
Explanation: The only missing range is [-3,-1], which becomes "-3->-1".



Example 4:
Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.



Example 5:
Input: nums = [-1], lower = -2, upper = -1
Output: ["-2"]



Constraints:
1) -10^9 <= lower <= upper <= 10^9
2) 0 <= nums.length <= 100
3) lower <= nums[i] <= upper
4) All the values of nums are unique.

"""

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def getRange(lower, upper):
            if lower == upper:
                return "{}".format(lower)
            else:
                return "{}->{}".format(lower, upper)

        ranges = []
        pre = lower - 1

        for i in range(len(nums) + 1):
            if i == len(nums):
                cur = upper + 1
            else:
                cur = nums[i]

            if cur - pre >= 2:
                ranges.append(getRange(pre + 1, cur - 1))

            pre = cur

        return ranges


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findMissingRanges([0,1,3,50,75], 0, 99), ["2","4->49","51->74","76->99"])
    test(solution.findMissingRanges([], 1, 1), ["1"])
    test(solution.findMissingRanges([], -3, -1), ["-3->-1"])
    test(solution.findMissingRanges([-1], -1, -1), [])
    test(solution.findMissingRanges([-1], -2, -1), ["-2"])
