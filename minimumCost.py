class Solution:
    def minimumCost(self, cost, w):
        n = len(cost)
        INF = float('inf')
        dp = [INF] * (w + 1)
        dp[0] = 0

        for i in range(n): # i+1 = weight of packet
            if cost[i] == -1:
                continue
            weight = i + 1
            c = cost[i]
            for curr_w in range(weight, w + 1):
                if dp[curr_w - weight]!= INF:
                    dp[curr_w] = min(dp[curr_w], dp[curr_w - weight] + c)

        return dp[w] if dp[w]!= INF else -1
