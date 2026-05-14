class Solution:
    def search(self, a, b):
        n = len(a)
        m = len(b)

        # Build LPS array
        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if b[i] == b[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # KMP Search
        ans = []
        i = 0  # index for a
        j = 0  # index for b

        while i < n:
            if a[i] == b[j]:
                i += 1
                j += 1

            if j == m:
                ans.append(i - j)
                j = lps[j - 1]

            elif i < n and a[i] != b[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return ans
