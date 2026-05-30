class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #cache = [False for _ in range(amount+1)]
        cache = {}
        def dfs(remaining):
            if remaining < 0:
                return float("inf")

            if remaining == 0:
                return 0

            if remaining in cache:
                return cache[remaining]
            
            min_coins = float("inf")
            for i in range(len(coins)):
                min_coins = min(
                    min_coins,
                    1 + dfs(remaining - coins[i])
                )

            cache[remaining] = min_coins

            return min_coins

        res = dfs(amount)
        if res == float("inf"):
            return -1
        else:
            return res
