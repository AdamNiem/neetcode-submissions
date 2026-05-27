class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(curr_sum):
            if curr_sum > n:
                return 0

            if curr_sum == n:
                return 1

            if curr_sum in cache:
                return cache[curr_sum]

            cache[curr_sum] = dfs(curr_sum + 1) + dfs(curr_sum + 2)
            return cache[curr_sum]
        
        return dfs(0)

        
        
        