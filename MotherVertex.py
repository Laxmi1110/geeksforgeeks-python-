class Solution:
    def findMotherVertex(self, V, edges):
        # Create adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)

        # DFS function
        def dfs(node, visited):
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, visited)

        # Step 1: Find candidate mother vertex
        visited = [False] * V
        candidate = -1

        for i in range(V):
            if not visited[i]:
                dfs(i, visited)
                candidate = i

        # Step 2: Verify candidate
        visited = [False] * V
        dfs(candidate, visited)

        # If candidate cannot reach all vertices
        if not all(visited):
            return -1

        # Step 3: Find smallest mother vertex
        result = candidate

        for i in range(candidate):
            visited = [False] * V
            dfs(i, visited)

            if all(visited):
                result = i
                break

        return result
