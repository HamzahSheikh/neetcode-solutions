class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        def add(index, num: List[int]):
            
            if index < 0:
                num.insert(0, 1)
                return num[:]

            num[index] += 1

            if num[index] == 10:
                num[index] = 0
                return add(index-1, num[:])
            
            return num[:]

        return add(len(digits)-1, digits[:])
        