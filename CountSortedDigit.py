class Solution:
    def validGroups(self, s):
        n = len(s)

        dp = [[-1] * 901 for _ in range(n + 1)]

        def solve(index, prev_sum):
            # Reached end of string
            if index == n:
                return 1

            if dp[index][prev_sum] != -1:
                return dp[index][prev_sum]

            ans = 0
            curr_sum = 0

            # Try all possible partitions
            for j in range(index, n):
                curr_sum += int(s[j])

                # Non-decreasing condition
                if curr_sum >= prev_sum:
                    ans += solve(j + 1, curr_sum)

            dp[index][prev_sum] = ans
            return ans

        return solve(0, 0)
