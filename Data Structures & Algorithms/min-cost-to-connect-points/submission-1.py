class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        seen = set()
        heap = []
        n = len(points)

        total = 0
        
        heapq.heappush(heap, (0, points[0]))

        while len(seen) < n:
            
            dist_i, coord = heapq.heappop(heap)
            xi, yi = coord

            if (xi, yi) in seen:
                continue

            seen.add((xi, yi))
            total += dist_i

            for xj, yj in points:
                dist = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(heap, (dist, (xj, yj)))

        return total



