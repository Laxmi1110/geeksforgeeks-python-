class Solution:
    
    def dfs(self, i, j, grid, vis):
        
        n = len(grid)
        m = len(grid[0])

        vis[i][j] = 1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in directions:
            ni = i + dr
            nj = j + dc

            if (0 <= ni < n and
                0 <= nj < m and
                grid[ni][nj] == 1 and
                vis[ni][nj] == 0):

                self.dfs(ni, nj, grid, vis)

    def cntOnes(self, grid):

        n = len(grid)
        m = len(grid[0])

        vis = [[0] * m for _ in range(n)]

        # Traverse first and last column
        for i in range(n):

            if grid[i][0] == 1 and vis[i][0] == 0:
                self.dfs(i, 0, grid, vis)

            if grid[i][m - 1] == 1 and vis[i][m - 1] == 0:
                self.dfs(i, m - 1, grid, vis)

        # Traverse first and last row
        for j in range(m):

            if grid[0][j] == 1 and vis[0][j] == 0:
                self.dfs(0, j, grid, vis)

            if grid[n - 1][j] == 1 and vis[n - 1][j] == 0:
                self.dfs(n - 1, j, grid, vis)

        count = 0

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1 and vis[i][j] == 0:
                    count += 1

        return count
