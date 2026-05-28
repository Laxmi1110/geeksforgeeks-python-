from collections import defaultdict

class Solution:
    def verticalSum(self, root):
        mp = defaultdict(int)

        # DFS traversal
        def solve(node, hd):
            if not node:
                return

            mp[hd] += node.data

            solve(node.left, hd - 1)
            solve(node.right, hd + 1)

        solve(root, 0)

        # Return sums from leftmost to rightmost
        return [mp[i] for i in sorted(mp)]
