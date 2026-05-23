class Solution:
    
    def solve(self, root):
        
        if root is None:
            return 0

        old_val = root.data

        left_sum = self.solve(root.left)
        right_sum = self.solve(root.right)

        root.data = left_sum + right_sum

        return old_val + root.data

    def toSumTree(self, root):
        
        self.solve(root)
