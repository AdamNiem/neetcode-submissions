from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if edges == []: 
            return True

        neighbor_map = {i:[] for i in range(n)}
        in_degrees = [0 for i in range(n)]
        max_indegree_node = -1

        for n1, n2 in edges:
            neighbor_map[n1].append(n2)
            neighbor_map[n2].append(n1)
            in_degrees[n1] += 1
            in_degrees[n2] += 1
            if in_degrees[n1] > max_indegree_node:
                max_indegree_node = n1
            if in_degrees[n2] > max_indegree_node:
                max_indegree_node = n2

        visited = set()

        def dfs(node, prevNode):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in neighbor_map[node]:
                if neighbor == prevNode:
                    continue
                if not dfs(neighbor, node):
                    return False
            #visited.remove(node)
            return True

        if not dfs(max_indegree_node, -1):
            return False

        print(visited)
        if len(visited) != n:
            print(len(visited))
            return False

        return True
