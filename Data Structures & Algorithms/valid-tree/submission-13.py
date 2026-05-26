from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for i in range(n)]

        if n == 1 and edges == [[0,0]]:
            return False

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        #want bfs solution
        queue = deque([0])
        visited = set()
        prev_node = -1
        while queue:
            node = queue.popleft()
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == prev_node or neighbor in visited:
                    continue
                queue.append(neighbor)

        return len(visited) == n