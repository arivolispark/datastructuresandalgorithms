class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        frequency_map_1, frequency_map_2 = {}, {}
        
        for num in nums1:
            if num in frequency_map_1:
                frequency_map_1[num] = frequency_map_1.get(num) + 1
            else:
                frequency_map_1[num] = 1
        
        for num in nums2:
            if num in frequency_map_2:
                frequency_map_2[num] = frequency_map_2.get(num) + 1
            else:
                frequency_map_2[num] = 1

        for k1, v1 in frequency_map_1.items():
            if k1 in frequency_map_2:
                result.append(k1)

        return result
