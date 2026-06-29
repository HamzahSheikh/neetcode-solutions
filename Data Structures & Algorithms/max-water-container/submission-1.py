class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0

        for i in range(len(heights)):

            l = i
            r = i + 1

            while r < len(heights):
                #a = bh
                b = r - l
                h = min(heights[l], heights[r])
                a = b*h

                maxArea = max(maxArea, a)
                r+=1

        return maxArea

        



        