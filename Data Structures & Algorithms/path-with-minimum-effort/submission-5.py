class Solution:
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        def proccessNextNode(currEffort, newRow, newCol):
            newEffort = heights[newRow][newCol]
            netEffort = abs(newEffort - currEffort)
            netMaxEffort = max(netEffort, effort)
            heapq.heappush(heap, (netMaxEffort, (newRow, newCol)))

        start = (0, (0, 0))
        maxRow = len(heights) - 1
        maxCol = len(heights[0]) - 1

        seen = set()

        heap = []

        heapq.heappush(heap, start)

        while heap:

            effort, coords = heapq.heappop(heap)
            
            if coords in seen:
                continue
            
            seen.add(coords)

            row = coords[0]
            col = coords[1]
            currEffort = heights[row][col]

            if row == maxRow and col == maxCol:
                return effort
            
            #right
            if col < maxCol:
                newRow, newCol = row, col+1
                proccessNextNode(currEffort, newRow, newCol)
            
            #left
            if col > 0:
                newRow, newCol = row, col-1
                proccessNextNode(currEffort, newRow, newCol)

            #up
            if row > 0:
                newRow, newCol = row-1, col
                proccessNextNode(currEffort, newRow, newCol)

            #down
            if row < maxRow:
                newRow, newCol = row+1, col
                proccessNextNode(currEffort, newRow, newCol)

        return None

            

        