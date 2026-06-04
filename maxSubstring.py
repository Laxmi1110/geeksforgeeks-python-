class Solution:
    def maxSubstring(self, s):
        max_sum = 0
        curr_sum = 0
        has_zero = False
        
        for ch in s:
            if ch == '0':
                has_zero = True
                val = 1
            else:
                val = -1
                
            curr_sum = max(val, curr_sum + val)
            max_sum = max(max_sum, curr_sum)
        
        # Per problem: if all 1s, return -1
        return -1 if not has_zero else max_sum
