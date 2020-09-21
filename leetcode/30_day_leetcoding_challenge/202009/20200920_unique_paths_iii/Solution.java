/*
Title: Unique Paths III

On a 2-dimensional grid, there are 4 types of squares:
1) 1 represents the starting square.  There is exactly one starting square.
2) 2 represents the ending square.  There is exactly one ending square.
3) 0 represents empty squares we can walk over.
3) -1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that
walk over every non-obstacle square exactly once.



Example 1:
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)



Example 2:
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)



Example 3:
Input: [[0,1],[2,0]]
Output: 0
Explanation:
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.


Note:
1) 1 <= grid.length * grid[0].length <= 20
*/



class Solution {
    int totalPath = 0;

    public int uniquePathsIII(int[][] grid) {
        int totalZero = 0;

        for (int i=0; i<grid.length; i++) {
            for (int j=0; j<grid[0].length; j++) {
                if (grid[i][j] == 0) {
                    totalZero++;
                }
            }
        }

        for (int i=0; i<grid.length; i++) {
            for (int j=0; j<grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    dfs(grid, i, j, totalZero);
                }
            }
        }

        return totalPath;
    }

    void dfs(int[][] grid, int i, int j, int totalZero) {
        if (i < 0 || j < 0 || i > grid.length - 1 || j > grid[0].length - 1 || grid[i][j] == -1 ||
        (grid[i][j] == 2 && totalZero != 0) || grid[i][j] == 99) {
            return;
        }

        if (grid[i][j] == 2 && totalZero == 0) {
            totalPath++;
        }

        if (grid[i][j] == 0) {
            totalZero--;
        }

        int temp = grid[i][j];
        grid[i][j] = 99;

        dfs(grid, i + 1, j, totalZero);
        dfs(grid, i - 1, j, totalZero);
        dfs(grid, i, j + 1, totalZero);
        dfs(grid, i, j - 1, totalZero);

        grid[i][j] = temp;
    }
}
