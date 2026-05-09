class Solution:
    def maxProfit(self, x, y, a, b):
        
        n = len(a)
        
        tasks = []
        
        for i in range(n):
            tasks.append((a[i], b[i]))
        
        # Sort by absolute difference in descending order
        tasks.sort(key=lambda t: abs(t[0] - t[1]), reverse=True)
        
        profit = 0
        
        for A, B in tasks:
            
            if (A >= B and x > 0) or y == 0:
                profit += A
                x -= 1
            else:
                profit += B
                y -= 1
        
        return profit
