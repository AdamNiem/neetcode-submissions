class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 #base case
        for remaining in range(1, len(dp)):
            for coin in coins:
                if remaining - coin >= 0:
                    dp[remaining] = min(
                        dp[remaining],
                        1 + dp[remaining - coin]
                    )
        
        return -1 if dp[amount] == (amount + 1) else dp[amount]