class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        result = 0
        q = collections.deque()

        for i in range(len(nums)):
            while q and i > q[0] + k - 1:
                q.popleft()

            if (nums[i] + len(q)) % 2 == 0:
                if i + k > len(nums):
                    return -1
                result += 1
                q.append(i)

        return result
        

    def minKBitFlips_1(self, nums: List[int], k: int) -> int:
        result = 0
        cur_window_flips = 0

        for i in range(len(nums)):
            if i - k >= 0 and nums[i - k] == 2:
                cur_window_flips -= 1

            if (nums[i] + cur_window_flips) % 2 == 0:
                if i + k > len(nums):
                    return -1
                result += 1
                cur_window_flips += 1
                nums[i] = 2

        return result
