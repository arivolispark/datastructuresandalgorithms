class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        length = len(nums)

        left_lis = [1] * length
        right_lis = [1] * length

        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    left_lis[i] = max(left_lis[i], left_lis[j] + 1)

        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                if nums[i] > nums[j]:
                    right_lis[i] = max(right_lis[i], right_lis[j] + 1)

        max_bitonic_len = max(
            (left + right - 1)
            for left, right in zip(left_lis, right_lis)
            if left > 1 and right > 1
        )

        return length - max_bitonic_len
