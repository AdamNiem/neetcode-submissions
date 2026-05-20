class Solution:
    class Trie:
        class Node:
            def __init__(self):
                self.hashmap = {}
                self.end_of_word = False
                self.visited = 0

        def __init__(self):
            self.root_node = self.Node()

        def add_word(self, word):
            node = self.root_node
            for c in word:
                if c not in node.hashmap:
                    node.hashmap[c] = self.Node()
                node = node.hashmap[c]
            node.end_of_word = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = self.Trie()
        for word in words:
            trie.add_word(word)

        board_width = len(board[0])
        board_height = len(board)

        res = set()

        def dfs(i, j, root, word, visited) -> None:
            nonlocal res
            node = root if root else trie.root_node

            if i < 0 or j < 0 or i >= board_width or j >= board_height:
                return

            tile_index = j * board_width + i
            
            if tile_index in visited:
                return
            
            c = board[j][i]
            if c not in node.hashmap:
                return
            
            node = node.hashmap[c]
            word += c
            visited.add(tile_index)
    
            dfs(i + 1, j, node, word, visited)
            dfs(i, j + 1, node, word, visited)
            dfs(i - 1, j, node, word, visited)
            dfs(i, j - 1, node, word, visited)

            visited.remove(tile_index)

            if node.end_of_word:
                res.add(word)
                
            
        for idx in range(board_width):
            for jdx in range(board_height):
                dfs(idx, jdx, trie.root_node, "", set())

        return list(res)
