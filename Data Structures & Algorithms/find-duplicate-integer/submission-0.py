class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        items = set()

        for x in nums:
            
            if x in items:
                return x

            items.add(x)
        
        return None
        