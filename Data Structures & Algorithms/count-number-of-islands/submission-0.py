class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()

        maxRow = len(grid)
        maxCol = len(grid[0])

        def markIsland(row, col):
            
            if row >= maxRow or col >= maxCol or row < 0 or col < 0 or grid[row][col] != "1" or (row, col) in seen:
                return

            seen.add((row, col))
            
            markIsland(row+1, col)
            markIsland(row, col+1)
            markIsland(row-1, col)
            markIsland(row, col-1)

            return

        ans = 0
                
        
        for r in range(0, maxRow):
            for c in range(0, maxCol):
                curr = grid[r][c]

                if curr == "1" and (r, c) not in seen:
                    ans += 1
                    markIsland(r, c)
                
                seen.add((r, c))


        return ans