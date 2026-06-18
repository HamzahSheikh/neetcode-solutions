class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        network_map = {x:[] for x in range(1, n+1)}

        for time in times:
            source = time[0]
            target = time[1]
            time_req = time[2]

            network_map[source].append((time_req, target))

        heap = []
        seen = set()

        heapq.heappush(heap, (0, k))

        while heap:

            time, target = heapq.heappop(heap)

            if target in seen:
                continue

            seen.add(target)

            if len(seen) == n:
                return time

            for node in network_map[target]:
                node_time = node[0]
                node_target = node[1]

                new_time = node_time + time

                heapq.heappush(heap, (new_time, node_target))

        return -1


        