class Solution:
    def isSumOfConsecutive(self, n):
        # A number can be written as sum of >=2 consecutive 
        # positive numbers iff it's NOT a power of 2
        return n & (n - 1) != 0
