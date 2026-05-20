class Solution:
    class Trie:
        class Node:
            def __init__(self):
                self.hashmap = {}
                self.end_of_word = False

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

        res, visited = set(), set()

        def dfs(i, j, root, word):
            
            if i < 0 or j < 0 or i >= board_width or j >= board_height:
                return

            if (i, j) in visited:
                return

            c = board[j][i]
            node = root
            if c not in node.hashmap:
                return
            word += c
            node = node.hashmap[c]

            visited.add((i, j))
            
            dfs(i + 1,    j, node, word)
            dfs(i    , j + 1, node, word)
            dfs(i - 1,    j, node, word)
            dfs(i   , j - 1, node, word)

            visited.remove((i, j))

            if node.end_of_word:
                res.add(word)
            
        for i in range(0, board_width):
            for j in range(0, board_height):
                dfs(i, j, trie.root_node, "")

        return list(res)