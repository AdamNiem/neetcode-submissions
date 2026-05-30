class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #runtime: must traverse tree once to end so thats equal to amount / smallest coin? 
        #Or i assume the runtime is equal to all numerical combinations we can make
        #with the coins that is from 0 to amount so that would be n * k
        #where n is number of options of coins to use and k is number of ways to idk
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for remaining in range(1, len(dp)):
            for coin in coins:
                if remaining - coin >= 0:
                    dp[remaining] = min(
                        dp[remaining],
                        1 + dp[remaining - coin]
                    )

        res = dp[amount]
        if res == float("inf"):
            return -1
        else:
            return res
