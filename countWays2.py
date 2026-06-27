class Solution:
    def countWays(self, n, m):
        MOD = 10**9 + 7

        dp = [1] * (n + 1)
        dp[0] = 1

        for i in range(m, n + 1):
            dp[i] = (dp[i - 1] + dp[i - m]) % MOD

        return dp[n]
