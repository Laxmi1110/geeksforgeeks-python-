class Solution:
    def minOperations(self, arr):
        n = len(arr)

        pre = [0] * n
        pre[0] = arr[0]

        for i in range(1, n):
            pre[i] = pre[i - 1] + arr[i]

        ans = []

        for i in range(n):
            m = (i + 1) // 2

            left = arr[m] * (m + 1) - pre[m]

            right = (pre[i] - pre[m]) - arr[m] * (i - m)

            ans.append(left + right)

        return ans
