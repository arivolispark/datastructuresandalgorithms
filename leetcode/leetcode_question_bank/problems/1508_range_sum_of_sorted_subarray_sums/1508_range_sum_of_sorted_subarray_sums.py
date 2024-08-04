class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = []
        length = len(nums)
        sum = 0

        iteration = 0
        start = 0
        previous = 0
        while start < length:
            previous += nums[start]
            result.append(previous)
            start += 1

            if start == length:
                previous = 0
                iteration += 1
                start = iteration
        
        result.sort()
        
        for i in range(left - 1, right, 1):
            sum += result[i]

        return sum % (10 ** 9 + 7)
