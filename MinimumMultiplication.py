from collections import deque

class Solution:
    def minSteps(self, arr, start, end):
        
        if start == end:
            return 0

        MOD = 1000

        dist = [float('inf')] * MOD
        dist[start] = 0

        q = deque()
        q.append((start, 0))

        while q:
            node, steps = q.popleft()

            for num in arr:
                new_node = (node * num) % MOD

                if steps + 1 < dist[new_node]:
                    dist[new_node] = steps + 1

                    if new_node == end:
                        return steps + 1

                    q.append((new_node, steps + 1))

        return -1
