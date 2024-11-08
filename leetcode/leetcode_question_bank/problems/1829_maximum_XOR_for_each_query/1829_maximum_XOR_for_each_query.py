class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mx = (1 << maximumBit) - 1
        result = []
        xors = 0

        for num in nums:
            xors ^= num
            result.append(xors ^ mx)

        return result[::-1]
