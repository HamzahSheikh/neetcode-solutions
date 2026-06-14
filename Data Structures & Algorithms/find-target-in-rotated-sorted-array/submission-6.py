class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        # Strategy: if value at l < r, we know the list is ordered
        # Otherwise, we have technically two sorted lists

        # [3, 4, 5 ,6] and [1, 2]
        # if we can choose what list to look at, this will be trivial binary search

        while l <= r:

            mid = (l+r)//2
            val = nums[mid]

            if val == target:
                return mid

            if val >= nums[l]:
                # we can check right side with confidence
                if target > val or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < val or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


        