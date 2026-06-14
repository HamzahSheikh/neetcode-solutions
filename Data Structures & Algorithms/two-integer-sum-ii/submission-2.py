class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, x in enumerate(numbers):
            needed = target - x

            if needed in seen:
                return [seen[needed]+1, i+1]
            
            seen[x] = i
        
            
            