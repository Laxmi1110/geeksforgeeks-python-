class Solution:
    def makeBeautiful(self, arr):
        stack = []
        
        for num in arr:
            # If stack is not empty and signs are different
            if stack and ((stack[-1] >= 0 and num < 0) or (stack[-1] < 0 and num >= 0)):
                stack.pop()
            else:
                stack.append(num)
        
        return stack
