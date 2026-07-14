class Solution:
    def find(self, arr):
        # we need smallest x > 0 such that x = 2*x - arr[i] never < 0
        x = 0
        # go backwards: x_prev = ceil((x_next + arr[i]) / 2)
        for a in reversed(arr):
            x = (x + a + 1) // 2 # ceil division
        return x
