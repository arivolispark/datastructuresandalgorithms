class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        champion_score, champion = 0, 0
        if grid:
            r, c = len(grid), len(grid[0])
            for i in range(r):
                player_score = 0
                for j in range(c):
                    player_score += grid[i][j]
                if player_score > champion_score:
                    champion_score = player_score
                    champion = i
        return champion
