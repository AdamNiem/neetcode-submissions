class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        #could also binary search for pivot (log n)
        #then binary search for value given pivot (log n)
        #so that would be asymptotically (log n)

        while l <= r:
            if nums[l] <= nums[r]:
                #then we are in one sorted portion so can do normal binary search
                m = (l + r) // 2
                print(m)
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    r = m - 1
                if nums[m] < target:
                    l = m + 1
            elif nums[l] > nums[r]:
                #then we are still in both sorted portions and dont know the pivot
                #so then we need to search in upper half and lower half
                if nums[l] < target:
                    l += 1
                elif nums[r] > target:
                    r -= 1
                elif nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    l += 1

        return -1

        #case:
        # [3, 4, 5, 6, 1, 2]

        # [3, 4, 5] [6, 1, 2]

        #target 1