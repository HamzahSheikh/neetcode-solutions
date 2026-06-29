class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        items = {} # 1: 0, 2: 1, 3: 2, 

        #1, 2, 3, 1
        for i, v in enumerate(nums): # 1

            if v in items and (i - items[v]) <= k:
                return True

            items[v] = i

        return False
        