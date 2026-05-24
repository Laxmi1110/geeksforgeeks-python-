class Solution:
    def lastCoin(self, arr):
        left = 0
        right = len(arr) - 1

        # Remove coins until one remains
        while left < right:
            
            # Pick the larger coin from ends
            if arr[left] > arr[right]:
                left += 1
            else:
                right -= 1

        return arr[left]
