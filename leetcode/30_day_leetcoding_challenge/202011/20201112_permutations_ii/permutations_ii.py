"""
Title:  Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all 
possible unique permutations in any order.

 

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]



Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1) 1 <= nums.length <= 8
2) -10 <= nums[i] <= 10

"""


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        result = [[]]
        for n in nums:
            ls = []
            for ar in result:
                for i in range(len(ar) + 1):
                    ls.append(ar[:i] + [n] + ar[i:])
                    if i < len(ar) and ar[i] == n:
                        break
            result = ls
        return result        


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

