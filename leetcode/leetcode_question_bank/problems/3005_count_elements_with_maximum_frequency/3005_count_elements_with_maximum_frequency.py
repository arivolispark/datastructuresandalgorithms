import math

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency_map = {}
        max_frequency = -math.inf
        result = 0

        for num in nums:
            if num not in frequency_map:
                frequency_map[num] = 1
            else:
                frequency_map[num] = frequency_map.get(num) + 1
            max_frequency = max(max_frequency, frequency_map[num])
        
        for k, v in frequency_map.items():
            if v == max_frequency:
                result += v

        return result
