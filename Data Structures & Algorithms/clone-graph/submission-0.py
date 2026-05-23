"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque([node])
        clones = {}

        clones[node] = Node(node.val)

        while queue:
            curr_node = queue.popleft()

            for neighbor in curr_node.neighbors:
                #skip if already in list to prevent infinite loops
                if neighbor not in clones: 
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                clones[curr_node].neighbors.append(
                    clones[neighbor]
                )   

        return clones[node]
        




        