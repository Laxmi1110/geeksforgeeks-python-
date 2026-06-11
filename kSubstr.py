class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        n = len(s)
        if n % k != 0:
            return False
        
        from collections import Counter
        blocks = [s[i:i+k] for i in range(0, n, k)]
        freq = Counter(blocks)
        
        if len(freq) == 1:
            return True
        if len(freq) == 2:
            return 1 in freq.values()
        
        return False
