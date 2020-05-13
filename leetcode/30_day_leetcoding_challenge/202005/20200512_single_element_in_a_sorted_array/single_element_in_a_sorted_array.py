"""
Title:  Single Element in a Sorted Array

You are given a sorted array consisting of only integers where
every element appears exactly twice, except for one element which
appears exactly once. Find this single element that appears only once.



Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2


Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10


Note: Your solution should run in O(log n) time and O(1) space.

"""

from typing import List


class Solution:

    def singleNonDuplicate(self, nums: List[int]) -> int:
        if nums:
            start, end = 0, len(nums) - 1

            while start < end:
                mid = start + (end - start) // 2
                even_parts_flag = (end - mid) % 2 == 0

                if nums[mid + 1] == nums[mid]:
                    if even_parts_flag:
                        start = mid + 2
                    else:
                        end = mid - 1
                elif nums[mid - 1] == nums[mid]:
                    if even_parts_flag:
                        end = mid - 2
                    else:
                        start = mid + 1
                else:
                    return nums[mid]
            return nums[start]
        return None


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.singleNonDuplicate(None), None)
    test(solution.singleNonDuplicate([]), None)
    test(solution.singleNonDuplicate([3]), 3)
    test(solution.singleNonDuplicate([1, 1, 2]), 2)
    test(solution.singleNonDuplicate([1, 2, 2]), 1)
    test(solution.singleNonDuplicate([1, 1, 2, 3, 3]), 2)
    test(solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]), 2)
    test(solution.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]), 10)
