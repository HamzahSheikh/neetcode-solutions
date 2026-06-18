class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0
        rotten = deque()
        ans = 0

        len_row = len(grid)
        len_col = len(grid[0])

        for r in range(len_row):
            for c in range(len_col):
                
                curr = grid[r][c]
                
                if curr == 1:
                    fresh += 1
                if curr == 2:
                    rotten.append((r, c))



        while rotten and fresh > 0:
            new_fruit_to_infect = set()

            while rotten:
                curr = rotten.popleft()
                r = curr[0]
                c = curr[1]

                #check for freshFruit arround:
                #up
                if r - 1 >= 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    new_fruit_to_infect.add((r-1,c))
                    fresh -= 1
                
                #left
                if c - 1 >= 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    new_fruit_to_infect.add((r,c-1))
                    fresh -= 1
                
                #down
                if r + 1 < len_row and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    new_fruit_to_infect.add((r+1,c))
                    fresh -= 1
                
                #right
                if c + 1 < len_col and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    new_fruit_to_infect.add((r,c+1))
                    fresh -= 1

            for item in new_fruit_to_infect:
                rotten.append(item)

            ans += 1

        print(fresh, ans)

        return ans if fresh == 0 else -1
            


            
                
                    


        
        


        