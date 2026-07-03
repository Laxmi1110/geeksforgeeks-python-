class Solution:
    def waysToIncreaseLCSBy1(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)

        # prefix LCS
        pref = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i-1] == s2[j-1]:
                    pref[i][j] = pref[i-1][j-1] + 1
                else:
                    pref[i][j] = max(pref[i-1][j], pref[i][j-1])
        L = pref[n1][n2]

        # suffix LCS
        suff = [[0] * (n2 + 2) for _ in range(n1 + 2)]
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if s1[i] == s2[j]:
                    suff[i][j] = suff[i+1][j+1] + 1
                else:
                    suff[i][j] = max(suff[i+1][j], suff[i][j+1])

        res = 0
        for i in range(n1 + 1): # insert position in s1
            seen = [False] * 26
            for j in range(n2): # match with s2[j]
                ch = ord(s2[j]) - ord('a')
                if seen[ch]:
                    continue
                if pref[i][j] + 1 + suff[i][j+1] == L + 1:
                    seen[ch] = True
                    res += 1
        return res
