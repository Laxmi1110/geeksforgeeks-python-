class Solution:
    def check_elements(self, arr, start, end):
        
        s = set(arr)

        for num in range(start, end + 1):
            if num not in s:
                return False

        return True
