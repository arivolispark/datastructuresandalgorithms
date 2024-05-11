class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        result = float("inf")
        max_heap = []
        total_quality = 0

        buckets = sorted(zip(quality, wage), key=lambda x: x[1] / x[0])

        for i in range(len(quality)):
            total_quality += buckets[i][0]
            heappush(max_heap, -buckets[i][0])

            while len(max_heap) > k:
                top = -heappop(max_heap)
                total_quality -= top

            if len(max_heap) == k:
                spend = total_quality * (buckets [i][1] / buckets [i][0])
                result = min(spend, result)

        return result
