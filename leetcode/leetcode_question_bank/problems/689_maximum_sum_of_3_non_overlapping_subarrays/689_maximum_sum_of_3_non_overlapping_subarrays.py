class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1
        sums = [0] * n
        l = [0] * n
        r = [0] * n

        summ = 0
        for i, num in enumerate(nums):
            summ += num
            if i >= k:
                summ -= nums[i - k]
            if i >= k - 1:
                sums[i - k + 1] = summ

        maxIndex = 0
        for i in range(n):
            if sums[i] > sums[maxIndex]:
                maxIndex = i
            l[i] = maxIndex

        maxIndex = n - 1
        for i in range(n - 1, -1, -1):
            if sums[i] >= sums[maxIndex]:
                maxIndex = i
            r[i] = maxIndex

        result = [-1, -1, -1]

        for i in range(k, n - k):
            if (result[0] == -1 or
                sums[result[0]] + sums[result[1]] + sums[result[2]] <
                    sums[l[i - k]] + sums[i] + sums[r[i + k]]):
                result[0] = l[i - k]
                result[1] = i
                result[2] = r[i + k]

        return result
