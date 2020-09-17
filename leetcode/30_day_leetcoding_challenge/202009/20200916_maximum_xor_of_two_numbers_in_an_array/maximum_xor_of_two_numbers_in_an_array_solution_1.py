"""
Title: Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:
Input: [3, 10, 5, 25, 2, 8]
Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

"""


from typing import List


class Solution:

    def findMaximumXOR(self, nums: List[int]) -> int:

        max_xor = 0
        if nums:
            nums_len = len(nums)
            for i in range(nums_len):
                for j in range(i + 1, nums_len):
                    max_xor = max (nums[i] ^ nums[j], max_xor)
        return max_xor


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findMaximumXOR([3, 10, 5, 25, 2, 8]), 28)
