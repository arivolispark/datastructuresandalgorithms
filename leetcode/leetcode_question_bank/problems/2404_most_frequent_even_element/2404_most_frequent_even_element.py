import math

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_map = {}
        even_number = math.inf
        even_number_count = -math.inf

        if nums:
            for num in nums:
                if num % 2 == 0:
                    even_map[num] = even_map.get(num, 0) + 1

            if len(even_map) == 0:
                return -1
            
            for v in even_map.values():
                even_number_count = max(v, even_number_count)

            for k, v in even_map.items():
                if v == even_number_count:
                    even_number = min(k, even_number)

        return even_number
