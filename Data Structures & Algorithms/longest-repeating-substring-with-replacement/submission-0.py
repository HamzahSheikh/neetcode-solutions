class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        p1 = 0
        p2 = 0

        maxF = 0
        maxSize = 0
        counts = {}

        while p2 < len(s):
            
            counts[s[p2]] = counts.get(s[p2], 0) + 1
            maxF = max(maxF, counts[s[p2]])
            size = p2 - p1 + 1

            while (p2 - p1 + 1 - maxF) > k:
                counts[s[p1]] -= 1
                p1 += 1

            maxSize = max(maxSize, p2-p1+1)

            p2+=1

        return maxSize
            
            
            