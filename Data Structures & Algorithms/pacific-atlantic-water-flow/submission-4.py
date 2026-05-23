class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        island_width = len(heights[0])
        island_height = len(heights)

        res = []
        visited_pac, visited_atl = set(), set()

        def dfs(i, j, visited, prev_height):
            if i < 0 or j < 0 or i >= island_width or j >= island_height:
                return
            
            height = heights[j][i]
            if height < prev_height:
                return

            if (i, j) in visited:
                return

            visited.add((i, j))
            
            dfs(i + 1, j, visited, height)
            dfs(i - 1, j, visited, height)
            dfs(i, j + 1, visited, height)
            dfs(i, j - 1, visited, height)

        for col in range(0, island_width):
            dfs(col, 0, visited_pac, heights[0][col])
            dfs(col, island_height - 1, visited_atl, heights[island_height - 1][col])

        for row in range(0, island_height):
            dfs(0, row, visited_pac, heights[row][0])
            dfs(island_width - 1, row, visited_atl, heights[row][island_width - 1])

        for idx in range(0, island_width):
            for jdx in range(0, island_height):
                if (idx, jdx) in visited_atl and (idx, jdx) in visited_pac:
                    res.append([jdx, idx])
        
        return res