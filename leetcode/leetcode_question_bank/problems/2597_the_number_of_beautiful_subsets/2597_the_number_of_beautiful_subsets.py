import collections

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:        
        def recurse(index, counter):
            if index == len(nums):
                return 1

            total = 0

            # skip
            total += recurse(index + 1, counter)
 
            # take
            if counter[nums[index] - k] == 0 and counter[nums[index] + k] == 0:
                counter[nums[index]] += 1
                total += recurse(index + 1, counter)
                counter[nums[index]] -= 1
            return total

        return recurse(0, Counter()) - 1        
