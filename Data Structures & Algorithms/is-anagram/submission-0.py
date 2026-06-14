class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a = {}
        b = {}

        for x in s:
            if x not in a:
                a[x] = 1
            else:
                a[x]+=1
        
        for x in t:
            if x not in b:
                b[x] = 1
            else:
                b[x]+=1

        return a == b