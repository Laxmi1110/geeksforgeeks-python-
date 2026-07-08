from collections import deque

class Solution:
    def countCoordinates(self, mat):
        n = len(mat)
        m = len(mat[0])

        def bfs(starts):
            vis = [[False] * m for _ in range(n)]
            q = deque(starts)

            for x, y in starts:
                vis[x][y] = True

            dirs = [(1,0),(-1,0),(0,1),(0,-1)]

            while q:
                x, y = q.popleft()

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < n and 0 <= ny < m and
                        not vis[nx][ny] and
                        mat[nx][ny] >= mat[x][y]):
                        vis[nx][ny] = True
                        q.append((nx, ny))

            return vis

        p = []
        q = []

        for i in range(n):
            p.append((i, 0))
            q.append((i, m - 1))

        for j in range(m):
            p.append((0, j))
            q.append((n - 1, j))

        visP = bfs(p)
        visQ = bfs(q)

        ans = 0
        for i in range(n):
            for j in range(m):
                if visP[i][j] and visQ[i][j]:
                    ans += 1

        return ans
