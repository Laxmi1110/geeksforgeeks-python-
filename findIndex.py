class Solution:
    def findIndex(self, s: str) -> int:
        n = len(s)
        total_close = s.count(')')

        open_count = 0
        for k in range(n + 1):
            if open_count == total_close:
                return k

            if k < n:
                if s[k] == '(':
                    open_count += 1
                else:
                    total_close -= 1

        return 0 # fallback, though constraints guarantee an answer
