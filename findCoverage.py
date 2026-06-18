class Solution:
    def findCoverage(self, mat):
        n = len(mat)
        m = len(mat[0])
        coverage = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:

                    # Left
                    for k in range(j - 1, -1, -1):
                        if mat[i][k] == 1:
                            coverage += 1
                            break

                    # Right
                    for k in range(j + 1, m):
                        if mat[i][k] == 1:
                            coverage += 1
                            break

                    # Up
                    for k in range(i - 1, -1, -1):
                        if mat[k][j] == 1:
                            coverage += 1
                            break

                    # Down
                    for k in range(i + 1, n):
                        if mat[k][j] == 1:
                            coverage += 1
                            break

        return coverage
