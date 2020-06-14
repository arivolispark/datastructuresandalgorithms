"""
Title:  Largest Divisible Subset

Given a set of distinct positive integers, find the largest
subset such that every pair (Si, Sj) of elements in this subset
satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)


Example 2:
Input: [1,2,4,8]
Output: [1,2,4,8]

"""

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        nums.sort()

        result = [[num] for num in nums]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(result[i]) < len(result[j]) + 1:
                    result[i] = result[j] + [nums[i]]
        return max(result, key=len)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    testcase_inputs = [
        #[2,3,5]
        #[3,2,5]
        [5,3,2]
    ]

    testcase_outputs = [
        [[2], [3], [5]]
    ]

    for i in range(len(testcase_inputs)):
        actual_results = solution.largestDivisibleSubset(testcase_inputs[i])
        print(" actual_results: ", actual_results)

        if actual_results:
            expected_results = testcase_outputs[i]
            print(" expected_results: ", expected_results)

            match = False
            for i in range(len(expected_results)):
                if actual_results in expected_results:
                    test(actual_results, expected_results[i])
                    match = True
                    break
            if match is False:
                test(actual_results, expected_results)

        #print(" result: ", result)

    """
    for i in range(len(testcase_outputs)):
        #test(testcase_inputs[i], testcase_outputs[i])
        print(testcase_outputs[i])
    """

    """
    test(solution.largestDivisibleSubset([]), [])
    test(solution.largestDivisibleSubset([3,2,1]), [1,2])
    test(solution.largestDivisibleSubset([1,2,3]), [1,2])
    test(solution.largestDivisibleSubset([1,2,3]), [1,3])
    test(solution.largestDivisibleSubset([1,2,4,8]), [1,2,4,8])
    """
