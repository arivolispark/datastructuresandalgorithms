"""
Title:  1636. Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple
values have the same frequency, sort them in decreasing order.

Return the sorted array.



Example 1:
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.


Example 2:
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.


Example 3:
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]


Constraints:
1) 1 <= nums.length <= 100
2) -100 <= nums[i] <= 100

"""

from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result = []
        frequency_map, map_2 = {}, {}

        for i in range(len(nums)):
            frequency_map[nums[i]] = frequency_map.get(nums[i], 0) + 1

        for k, v in frequency_map.items():
            if v not in map_2:
                map_2[v] = [k]
            else:
                l = map_2[v]
                l.append(k)
                map_2[v] = l

        frequency_list = []
        for k, v in map_2.items():
            frequency_list.append(k)
            v.sort(reverse = True)

        frequency_list.sort()

        for i in range(len(frequency_list)):
            frequency = frequency_list[i]
            l = map_2[frequency]
            for j in range(len(l)):
                num = l[j]
                for k in range(frequency):
                    result.append(num)

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.frequencySort([1,1,2,2,2,3]), [3,1,1,2,2,2])
    test(solution.frequencySort([2,3,1,3,2]), [1,3,3,2,2])
    test(solution.frequencySort([-1,1,-6,4,5,-6,1,4,1]), [5,-1,4,4,-6,-6,1,1,1])
