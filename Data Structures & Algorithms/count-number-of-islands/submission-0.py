class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #for each '1' cell we need to dfs 
        #i like the idea about replacing visited cells with '#'
        #instead of storing in visited set or what not
        
        # easy solution would be for each island to mark all visited nodes
        # as '#' except for the first one because then we can just count 
        # num of 1s to get num of islands
        # however i think we could do better
        # on each '1' encountered replace with '#' that way 
        #we know the first '1' we hit has to be the only '1' we hit for that island
        #lets get leeting

        grid_width = len(grid[0])
        grid_height = len(grid)

        num_islands = 0
        hit_island = False

        def dfs(i, j):

            if i < 0 or j < 0 or i >= grid_width or j >= grid_height:
                return
            
            if grid[j][i] != "1":
                return

            nonlocal hit_island
            hit_island = True

            grid[j][i] = "#"

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        for i in range(0, grid_width):
            for j in range(0, grid_height):
                dfs(i, j)
                if hit_island:
                    num_islands += 1
                    hit_island = False

        return num_islands

        
        
