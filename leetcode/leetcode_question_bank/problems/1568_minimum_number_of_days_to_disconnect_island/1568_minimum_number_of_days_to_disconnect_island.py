class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # If the number of islands is not one, return 0 as removing any cell is unnecessary.
        if self.count_islands(grid) != 1:
            return 0
      
        # Get the dimensions of the grid
        num_rows, num_cols = len(grid), len(grid[0])
      
        # Iterate through each cell in the grid
        for row in range(num_rows):
            for col in range(num_cols):
                # Checking if changing the land cell to water changes the number of islands
                if grid[row][col] == 1:
                    # Change the land cell to water
                    grid[row][col] = 0
                    # If the number of islands is not one, return 1 as we have split the grid
                    
                    if self.count_islands(grid) != 1:
                        return 1
                    # Change the cell back to land for further exploration
                    grid[row][col] = 1
      
        # If we haven't returned before, it means changing any one cell won't split the grid
        # Thus, we need to change at least two cells, hence return 2
        return 2

    def count_islands(self, grid: List[List[int]]) -> int:
        # Helper function to perform Depth-First Search (DFS) to count the number of islands
        def dfs(row: int, col: int):
            grid[row][col] = 2  # Mark the currently visited land cell with a temporary marker
            # Define the four possible directions to move (left, right, up, down)
            directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            # Explore the neighboring cells using the possible directions
            for delta_row, delta_col in directions:
                next_row, next_col = row + delta_row, col + delta_col
                # Check if the next position is within bounds and is land
                if 0 <= next_row < num_rows and 0 <= next_col < num_cols and grid[next_row][next_col] == 1:
                    dfs(next_row, next_col)  # Continue DFS from this land cell

        # Get the dimensions of the grid
        num_rows, num_cols = len(grid), len(grid[0])
        island_count = 0  # Counter for the number of islands

        # Iterate through each cell in the grid and count the islands
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:  # If a land cell is found
                    dfs(row, col)  # Run DFS to mark the entire island
                    island_count += 1  # Increment the island count
      
        # Revert the temporary markers back to original land cells
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 2:
                    grid[row][col] = 1
      
        # Return the total number of islands found
        return island_count
