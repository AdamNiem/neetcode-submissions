class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0 for _ in nums]
        def dfs(i):
            # from 0 we can jump +1 or +2 n times to get to any house i
            if i >= len(nums):
                return 0
            
            if i == len(nums) - 1:
                return nums[i]
            
            if cache[i] != 0:
                return cache[i]
            
            cache[i] = max(
                nums[i] + dfs(i + 2), 
                dfs(i + 1)
            )

            return cache[i]
            
        dfs(0)
        return dfs(0)