class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen = set()
        maxRow = len(grid)-1
        maxCol = len(grid[0])-1
        maxSize = 0

        def countIsland(row, col) -> int:

            if row < 0 or row > maxRow or col < 0 or col > maxCol or (row, col) in seen:
                return 0            
            
            block = grid[row][col]
            seen.add((row, col))

            if block == 0:
                return 0

            return 1 + countIsland(row+1, col) + countIsland(row, col+1) + countIsland(row-1, col) + countIsland(row, col-1)

            
        for r in range(maxRow+1):
            for c in range(maxCol+1):
                maxSize = max(maxSize, countIsland(r, c))

        return maxSize