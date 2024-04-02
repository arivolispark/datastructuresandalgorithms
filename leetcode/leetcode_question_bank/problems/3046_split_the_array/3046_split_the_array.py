class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if nums:
            if len(nums) % 2 == 1:
                return False
            
            numbers_map = {}
            
            for num in nums:
                numbers_map[num] = numbers_map.get(num, 0) + 1
                
            for k, v in numbers_map.items():
                if v > 2:
                    return False
        
        return True
