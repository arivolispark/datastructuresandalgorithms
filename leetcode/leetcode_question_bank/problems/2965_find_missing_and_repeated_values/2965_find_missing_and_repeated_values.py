class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        map = {}
        duplicate, missing = 0, 0

        for i in range(m):
            for j in range(n):
                map[grid[i][j]] = map.get(grid[i][j], 0) + 1

        for i in range(1, (m * n) + 1):
            if i not in map:
                missing = i
            else:
                if map[i] == 2:
                    duplicate = i

        return [duplicate, missing]
