class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        flight_map = {i:[] for i in range(n)}
        
        for flight in flights:
            flight_org = flight[0]
            flight_dest = flight[1]
            flight_cost = flight[2]

            flight_map[flight_org].append((flight_cost, flight_dest))
        
        heap = []

        heapq.heappush(heap, (0, 0, src))

        count = 0

        while heap:
            cost, depth, ap = heapq.heappop(heap)

            if ap == dst:
                return cost

            if depth > k:
                continue

            for flight in flight_map[ap]:
                flight_cost = flight[0]
                flight_dest = flight[1]

                new_cost = flight_cost + cost

                heapq.heappush(heap, (new_cost, depth+1, flight_dest))



        return -1 

            



        