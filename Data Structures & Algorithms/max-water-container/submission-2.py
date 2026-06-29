class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            #a = bh
            b = r - l
            h = min(heights[l], heights[r])
            a = b*h
            maxArea = max(maxArea, a)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return maxArea

        



        