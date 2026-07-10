class Solution:
    def getCount(self, n):
        ans = 0
        twoN = 2 * n

        k = 2
        while k * (k + 1) // 2 <= n:
            if twoN % k == 0:
                t = twoN // k - k + 1
                if t > 0 and t % 2 == 0:
                    ans += 1
            k += 1

        return ans
