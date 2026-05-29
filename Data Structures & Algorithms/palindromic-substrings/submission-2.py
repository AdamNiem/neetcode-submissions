class Solution:
    def countSubstrings(self, s: str) -> int:
        #two options, dp but it will be n^2 memory and runtime
        # now we do dp solution using tabulation
        n = len(s)
        palindromes = []
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    palindromes.append(s[i:j+1])

        
        return len(palindromes)