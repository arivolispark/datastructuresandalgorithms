class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        map = {}
        
        for num in nums:
            if not num in map:
                map[num] = num
            else:
                del map[num]

        for key in map.keys():
            result.append(key)

        return result
