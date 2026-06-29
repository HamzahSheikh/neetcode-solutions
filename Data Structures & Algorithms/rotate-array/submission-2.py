class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dict_prev = {}

        for i in range(len(nums)):
            
            whereToSwap = (i+k)%len(nums)
            dict_prev[whereToSwap] = nums[whereToSwap]

            if i in dict_prev:
                nums[whereToSwap] = dict_prev[i]
            else:
                nums[whereToSwap] = nums[i]


        