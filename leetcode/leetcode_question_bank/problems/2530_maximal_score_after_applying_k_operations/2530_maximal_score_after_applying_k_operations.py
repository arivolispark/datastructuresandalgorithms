class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        result = 0
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        for _ in range(k):
            num = -heapq.heappop(maxHeap)
            result += num
            heapq.heappush(maxHeap, -math.ceil(num / 3))

        return result
