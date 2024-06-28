class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        total = 0
        degrees = [0] * n

        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1
  
        degrees.sort(reverse=True)

        for i, x in enumerate(degrees):
            total += (n - i) * x

        return total
