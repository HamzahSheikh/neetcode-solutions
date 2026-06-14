class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        #First we need to determine how to calculate closest point
        #sqrt(x^2 + y^2)

        distances = []
        distance_map = {}

        for i, point in enumerate(points):
            a = point[0]
            b = point[1]

            distance = pow(pow(a,2)+pow(b,2), 0.5)

            heapq.heappush(distances, distance)
            
            if distance in distance_map:
                distance_map[distance].append(i)
            else:
                distance_map[distance] = [i]


        i = 0
        ans = []
        while i < k:
            ans_distance = heapq.heappop(distances) 
            ans_index = distance_map[ans_distance].pop()
            ans.append(points[ans_index])
            i+=1
        
        return ans
            
            
        