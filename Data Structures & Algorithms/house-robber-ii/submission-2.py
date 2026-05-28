class Solution:
    #now we do a top down dp solution using a cache
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 0:
            return 0

        cache = [0 for _ in nums] #store max val found up to that point

        def dfs(i, curr_sum, exclude_end = False):
            if i >= len(nums):
                return 0

            if i == len(nums) - 1 and exclude_end:
                return 0

            if cache[i] != 0:
                return cache[i]

            cache[i] = max(
                dfs(i + 1, 0, exclude_end),
                dfs(i + 2, curr_sum, exclude_end) + nums[i]
            )

            return cache[i]

        res = dfs(0, 0, True)
        #reset cache
        cache = [0 for _ in nums]
        return max(res, dfs(1, 0))

        '''
        return max(
            dfs(0, 0, True),
            dfs(1, 0)
        )
        '''
