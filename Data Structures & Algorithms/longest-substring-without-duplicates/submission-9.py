class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = {}
        maxStreak = 0
        p1 = 0
        p2 = 0

        while p2 < len(s):

            if s[p2] in subs and subs[s[p2]] >= p1:
                p1 = subs[s[p2]] + 1
            
            subs[s[p2]] = p2
            maxStreak = max(maxStreak, (p2 - p1) + 1)

            p2+=1

        return maxStreak
