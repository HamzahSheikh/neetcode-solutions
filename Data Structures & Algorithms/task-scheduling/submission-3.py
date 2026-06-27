class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = defaultdict(int)
        heap = []
        queue = deque()
        cycle = 0

        for x in tasks:
            count[x] += 1

        for x in count:
            heapq.heappush(heap, -count[x])

        while heap or queue:
            cycle += 1

            if heap:
                count = heapq.heappop(heap)
                if count < -1:
                    queue.append((cycle + n, count+1))
            
            #check if queue item is ready
            if queue and queue[0][0] <= cycle:
                val = queue.popleft()
                heapq.heappush(heap, val[1])
            
        return cycle


        #priority -> start with tasks with highest count
        #         -> if on cooldown, start with next highest
