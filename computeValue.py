class Solution:
    def computeValue(self, n):
        MOD = 10**9 + 7
        N = 2 * n

        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i-1] * i % MOD

        def modinv(x):
            return pow(x, MOD - 2, MOD)

        num = fact[N]
        den = fact[n] * fact[n] % MOD
        ans = num * modinv(den) % MOD
        return ans
