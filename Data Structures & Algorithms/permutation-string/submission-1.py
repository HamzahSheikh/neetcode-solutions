class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0
        r = len(s1) - 1

        if len(s1) > len(s2):
            return False

        dicts1 = {}

        for x in s1:
            dicts1[x] = dicts1.get(x, 0) + 1

        dicts2 = {}

        for i, x in enumerate(s2):
            
            if i > r:
                break
            
            dicts2[x] = dicts2.get(x, 0) + 1


        while r < len(s2):

            if dicts1 == dicts2:
                return True


            l += 1
            r += 1

            if r < len(s2):
                dicts2[s2[l-1]] = dicts2[s2[l-1]] - 1
                dicts2[s2[r]] = dicts2.get(s2[r], 0) + 1
                
                if dicts2[s2[l-1]] <= 0:
                    del dicts2[s2[l-1]]
                    
        return False
        return False
        