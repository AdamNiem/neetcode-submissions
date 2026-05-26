from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for i in range(n)]

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visited_global = set()
        num_trees = 0

        def bfs(startNode):
            visited = set()
            queue = deque([startNode])
            while queue:
                node = queue.popleft()
                visited.add(node)
                for neighbor in adj_list[node]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)

            nonlocal num_trees
            
            found = False
            for ele in visited:
                if ele not in visited_global and not found:
                    num_trees += 1
                    found = True
                visited_global.add(ele)

        for node in range(n):
            if node not in visited_global:
                bfs(node)
        
        return num_trees

        
        