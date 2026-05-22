class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited, found = set(), False

        board_width = len(board[0])
        board_height = len(board)
        
        def dfs(i, j, res):
            nonlocal found, visited

            if i < 0 or j < 0 or i >= board_width or j >= board_height:
                return

            tile_pos = board_width * j + i
            if tile_pos not in visited:
                res += board[j][i]
            else:
                return

            if res == word:
                found = True
                return

            """found_yet = True
            for i in len(res):
                if i >= len(word) or res[i] != word[i]:
                    found_yet = False
                    return
            if found_yet:
                found = True
                return"""

            visited.add(tile_pos) #prevent going to same cell twice in a word

            dfs(i + 1, j, res)
            dfs(i, j + 1, res)
            dfs(i - 1, j, res)
            dfs(i, j - 1, res)

            visited.remove(tile_pos)

        for row in range(0, board_height):
            for col in range(0, board_width):
                dfs(col, row, "")

        return found