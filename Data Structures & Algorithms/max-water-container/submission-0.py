class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # naive solution:
        # O(N^2) -> brute force check, double loop and save the max size

        p1 = 0
        p2 = len(heights) - 1

        maxsize = 0

        while p1 < p2:
            
            size = (p2 - p1)*min(heights[p1], heights[p2])

            if heights[p1] > heights[p2]:
                p2-=1
            else:
                p1+=1

            maxsize = max(maxsize, size)

        return maxsize        