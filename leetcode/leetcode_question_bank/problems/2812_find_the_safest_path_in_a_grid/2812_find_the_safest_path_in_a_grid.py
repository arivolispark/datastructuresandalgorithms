from typing import List
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        length = len(grid)
        INFINITY =  10 ** 20
        safety = [[INFINITY] * length for _ in range(length)]

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        q = deque()

        for i in range(length):
            for j in range(length):
                if grid[i][j] == 1:
                    safety[i][j] = 0
                    q.append((0, i, j))


        while len(q) > 0:
            d, x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < length and 0 <= ny < length and safety[nx][ny] == INFINITY:
                    safety[nx][ny] = d + 1
                    q.append((d + 1, nx, ny))

        visited = [[False] * length for _ in range(length)]
        q = deque()
        q.append((safety[0][0], 0, 0))
        visited[0][0] = True

        while len(q) > 0:
            d, x, y = q.popleft()

            if x == length - 1 and y == length - 1:
                return d

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < length and 0 <= ny < length and not visited[nx][ny]:
                    visited[nx][ny] = True

                    if d <= safety[nx][ny]:
                        q.appendleft((d, nx, ny))
                    else:
                        q.append((safety[nx][ny], nx, ny))

        return -1
