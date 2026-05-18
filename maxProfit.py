class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update minimum buying price
            min_price = min(min_price, price)

            # Calculate profit
            profit = price - min_price

            # Update maximum profit
            max_profit = max(max_profit, profit)

        return max_profit
