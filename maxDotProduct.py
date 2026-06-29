class Solution:
    def maxDotProduct(self, a, b):
        n = len(a)
        m = len(b)

        next_row = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            curr = [0] * (m + 1)

            for j in range(m - 1, -1, -1):
                if n - i < m - j:
                    curr[j] = float('-inf')
                else:
                    take = a[i] * b[j] + next_row[j + 1]
                    skip = next_row[j]
                    curr[j] = max(take, skip)

            next_row = curr

        return next_row[0]
