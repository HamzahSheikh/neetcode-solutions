class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        seen = set()

        for x in nums:
            converted = -1 * x
            heapq.heappush(heap, converted)


        i = 0
        ans = None

        while i < k:
            ans = -1 * heapq.heappop(heap)
            i+=1

        return ans

        