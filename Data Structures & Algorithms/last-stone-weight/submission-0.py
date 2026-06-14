class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heaviest = []

        for x in stones:
            heapq.heappush(heaviest, -1*x)

        while len(heaviest) > 1:
            big_1 = -1*heapq.heappop(heaviest)
            big_2 = -1*heapq.heappop(heaviest)

            remaining = big_1 - big_2

            if remaining > 0:
                heapq.heappush(heaviest, -1*remaining)

        if len(heaviest) > 0:
            return -1*heaviest[0]
        return 0

        
        