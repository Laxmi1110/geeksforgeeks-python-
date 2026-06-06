class Solution:
    def numWays(self, n: int, m: int) -> int:
        total = n * m * (n * m - 1)
        
        attack = 0
        if n > 1 and m > 2:
            attack += 4 * (n - 1) * (m - 2)
        if n > 2 and m > 1:
            attack += 4 * (n - 2) * (m - 1)
            
        return total - attack
