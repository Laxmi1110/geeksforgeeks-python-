class Solution:
    def kSubstr(self, s, k):
        n = len(s)

        if n % k != 0:
            return False

        freq = {}

        for i in range(0, n, k):
            block = s[i:i+k]
            freq[block] = freq.get(block, 0) + 1

        max_freq = max(freq.values())
        total_blocks = n // k

        return max_freq >= total_blocks - 1
