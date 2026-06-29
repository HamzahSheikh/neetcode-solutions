class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        closest = -1
        closest_diff = float('inf')


        for i, v in enumerate(arr):
            
            diff = abs(x-v)
            
            if diff < closest_diff:
                closest_diff = diff
                closest = i

        
        l = closest
        r = closest

        while (r - l) < k-1 and (l >= 0 or r < len(arr)):

            if l-1 < 0:
                r+=1
                continue
            
            if r+1 >= len(arr):
                l-=1
                continue

            diff_r = abs(arr[r+1] - x)
            diff_l = abs(arr[l-1] - x)

            if diff_r < diff_l:
                r+=1
            else:
                l-=1

        return arr[l:r+1]
            
        