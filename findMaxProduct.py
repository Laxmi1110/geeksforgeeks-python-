class Solution:
    def findMaxProduct(self, arr):
        MOD = 1000000007
        n = len(arr)

        if n == 1:
            return arr[0] % MOD

        neg_count = 0
        zero_count = 0
        max_neg = -11
        product = 1

        for x in arr:
            if x == 0:
                zero_count += 1
            else:
                product *= x

            if x < 0:
                neg_count += 1
                max_neg = max(max_neg, x)

        # All zeros
        if zero_count == n:
            return 0

        # If there is exactly one negative and all others are zero
        if neg_count == 1 and zero_count + neg_count == n:
            return 0

        # If odd number of negatives, remove the negative
        # with smallest absolute value (largest negative value)
        if neg_count % 2 == 1:
            product //= max_neg

        return product % MOD
