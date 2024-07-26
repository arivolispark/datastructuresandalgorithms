class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def getMapped(num: int) -> int:
            mapped_num = []
            for ch in str(num):
                mapped_num.append(str(mapping[ord(ch) - ord('0')]))
            return int(''.join(mapped_num))
        result = [(getMapped(num), i, num) for i, num in enumerate(nums)]
        return [num for _, i, num in sorted(result)]
