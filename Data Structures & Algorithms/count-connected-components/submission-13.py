from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for i in range(n)]
        visited = set()

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        res = 0
        def dfs(startNode):
            for neighbor in adj_list[startNode]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    

        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        
        return res

        
        