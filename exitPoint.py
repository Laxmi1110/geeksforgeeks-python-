class Solution:
    def exitPoint(self, mat):
        n = len(mat)
        m = len(mat[0])
        r, c = 0, 0
        dr, dc = 0, 1 # start moving right

        while True:
            if mat[r][c] == 1:
                mat[r][c] = 0
                dr, dc = dc, -dr # clockwise: right->down->left->up

            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                return [r, c]

            r, c = nr, nc
