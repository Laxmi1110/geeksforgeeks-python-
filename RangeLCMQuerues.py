from math import gcd

class Solution:

    def lcm(self, a, b):
        return (a * b) // gcd(a, b)

    def build(self, node, start, end, arr):

        if start == end:
            self.seg[node] = arr[start]
            return

        mid = (start + end) // 2

        self.build(2 * node, start, mid, arr)
        self.build(2 * node + 1, mid + 1, end, arr)

        self.seg[node] = self.lcm(
            self.seg[2 * node],
            self.seg[2 * node + 1]
        )

    def update(self, node, start, end, idx, val):

        if start == end:
            self.seg[node] = val
            return

        mid = (start + end) // 2

        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)

        self.seg[node] = self.lcm(
            self.seg[2 * node],
            self.seg[2 * node + 1]
        )

    def query(self, node, start, end, l, r):

        if r < start or end < l:
            return 1

        if l <= start and end <= r:
            return self.seg[node]

        mid = (start + end) // 2

        left = self.query(2 * node, start, mid, l, r)
        right = self.query(2 * node + 1, mid + 1, end, l, r)

        return self.lcm(left, right)

    # Correct function name
    def RangeLCMQuery(self, arr, queries):

        n = len(arr)

        self.seg = [1] * (4 * n)

        self.build(1, 0, n - 1, arr)

        ans = []

        for q in queries:

            if q[0] == 1:

                _, idx, val = q

                self.update(1, 0, n - 1, idx, val)

            else:

                _, l, r = q

                ans.append(
                    self.query(1, 0, n - 1, l, r)
                )

        return ans
