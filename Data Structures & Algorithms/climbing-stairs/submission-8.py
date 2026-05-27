class Solution:
    def climbStairs(self, n: int) -> int:
        prev, prevprev = 1, 1

        for _ in range(n - 1):
            prev, prevprev = prev + prevprev, prev

        return prev