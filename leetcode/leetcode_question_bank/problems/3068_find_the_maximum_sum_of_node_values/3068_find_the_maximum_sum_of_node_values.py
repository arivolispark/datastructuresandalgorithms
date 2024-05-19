class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        result = 0
        num_of_nodes = len(nums)

        deltas = []
        for x in nums:
            deltas.append((x ^ k) - x)

        deltas.sort(reverse = True)

        total = sum(nums)
        result = total

        i = 0
        while i + 1 < num_of_nodes:
            total += deltas[i] + deltas[i + 1]
            result = max(result, total)
            i += 2

        return result
