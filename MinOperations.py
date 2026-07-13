MOD = 10**9 + 7

class Solution:
    def minOperations(self, b):
        n = len(b)

        # 1. Sieve for smallest prime factor
        spf = list(range(n + 1))
        for i in range(2, int(n**0.5) + 1):
            if spf[i] == i:
                for j in range(i*i, n + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        visited = [False] * (n + 1)
        max_prime_pow = {} # prime -> max exponent

        # 2. Find all cycles
        for i in range(1, n + 1):
            if not visited[i]:
                cur = i
                length = 0
                while not visited[cur]:
                    visited[cur] = True
                    cur = b[cur - 1] # b is 0-indexed
                    length += 1

                # 3. Factorize this cycle length
                temp = length
                while temp > 1:
                    p = spf[temp]
                    cnt = 0
                    while temp % p == 0:
                        temp //= p
                        cnt += 1
                    max_prime_pow[p] = max(max_prime_pow.get(p, 0), cnt)

        # 4. Answer = product of p^max_exp % MOD
        ans = 1
        for p, exp in max_prime_pow.items():
            ans = (ans * pow(p, exp, MOD)) % MOD

        return ans
