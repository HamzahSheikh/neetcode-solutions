class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        maxB = piles[-1]


        p1 = 1
        p2 = maxB
        ans = maxB

        while p1 <= p2:
            
            mid = (p1+p2)//2

            total_time = 0

            for pile in piles:
                total_time += -(-pile // mid) 
            
            if total_time <= h:
                ans = mid
                p2 = mid - 1
            else:
                p1 = mid + 1

        return ans




            

        # for i in range(1, maxB + 1):
            
        #     total_time = 0

        #     for pile in piles:
        #         total_time += -(-pile//i)

        #         if total_time > h:
        #             break

        #     if total_time <=  h:
        #         return i

        return maxB




        