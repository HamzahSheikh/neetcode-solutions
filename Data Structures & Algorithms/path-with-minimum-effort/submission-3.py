class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

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
                newEffort = heights[newRow][newCol]
                netEffort = abs(newEffort - currEffort)
                netMaxEffort = max(netEffort, effort)
                heapq.heappush(heap, (netMaxEffort, (newRow, newCol)))
            
            #left
            if col > 0:
                newRow, newCol = row, col-1
                newEffort = heights[newRow][newCol]
                netEffort = abs(newEffort - currEffort)
                netMaxEffort = max(netEffort, effort)
                heapq.heappush(heap, (netMaxEffort, (newRow, newCol)))

            #up
            if row > 0:
                newRow, newCol = row-1, col
                newEffort = heights[newRow][newCol]
                netEffort = abs(newEffort - currEffort)
                netMaxEffort = max(netEffort, effort)
                heapq.heappush(heap, (netMaxEffort, (newRow, newCol)))

            #down
            if row < maxRow:
                newRow, newCol = row+1, col
                newEffort = heights[newRow][newCol]
                netEffort = abs(newEffort - currEffort)
                netMaxEffort = max(netEffort, effort)
                heapq.heappush(heap, (netMaxEffort, (newRow, newCol)))

        return None

            

        