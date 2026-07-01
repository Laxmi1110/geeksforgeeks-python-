class Solution:
    def maxSumSubarray(self, arr):
        n = len(arr)
        no_skip = arr[0] # max sum ending here, no skip used
        skip_one = float('-inf') # max sum ending here, one skip used
        ans = arr[0]

        for i in range(1, n):
            # If we skip arr[i], we must take no_skip from i-1
            # If we don't skip arr[i], we can extend previous skip_one or no_skip
            skip_one = max(skip_one + arr[i], no_skip)
            no_skip = max(arr[i], no_skip + arr[i])
            ans = max(ans, no_skip, skip_one)

        return ans
