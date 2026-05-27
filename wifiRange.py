class Solution:
    def wifiRange(self, s, x):
        n = len(s)
        cover = [False] * n

        last = -10**9

        # Left to right
        for i in range(n):
            if s[i] == '1':
                last = i

            if i - last <= x:
                cover[i] = True

        last = 10**9

        # Right to left
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                last = i

            if last - i <= x:
                cover[i] = True

        return all(cover)
