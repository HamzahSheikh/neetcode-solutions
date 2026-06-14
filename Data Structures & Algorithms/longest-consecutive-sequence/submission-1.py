class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = set()
        seen = set()
        longStreak = 0

        for x in nums:
            n.add(x)

        for x in nums:
            streak = 1
            curr = x

            if x in seen:
                continue

            seen.add(x)

            while curr + 1 in n:
                streak += 1
                curr += 1
            
            if streak > longStreak:
                longStreak = streak

        return longStreak
                

        
        