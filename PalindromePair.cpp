class Solution:
    def palindromepair(self, arr):
        n = len(arr)

        for i in range(n):
            for j in range(n):

                if i != j:
                    s = arr[i] + arr[j]

                    if s == s[::-1]:
                        return True

        return False
