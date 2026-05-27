class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0 for i in nums]
        def dfs(i):
            if i >= len(nums):
                return 0

            if cache[i] != 0:
                return cache[i]

            cache[i] = max(
                nums[i] + dfs(i + 2),
                dfs(i + 1)
            )
            
            return cache[i]

        return dfs(0)