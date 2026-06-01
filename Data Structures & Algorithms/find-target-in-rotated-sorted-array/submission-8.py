class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        l, r = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]:
            #then search to right of pivot and including the pivot
            l = pivot
        else:
            #search to the left of the pivot
            r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1

        # [4, 5, 6, 7, -2, -1, 0, 1]

        # [2, 3, 4, 5, 0, 1]
