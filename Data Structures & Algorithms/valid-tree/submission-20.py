from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for i in range(n)]

        for n1, n2 in edges:
            if n1 == n2: return False
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        #want bfs solution
        queue = deque([0])
        visited = set()
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)

        return len(visited) == n