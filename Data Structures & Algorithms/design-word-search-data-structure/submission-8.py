class WordDictionary:
    class Node:
        def __init__(self):
            self.hashmap = {}
            self.end_of_word = False

    def __init__(self):
        self.root_node = self.Node()

    def addWord(self, word: str) -> None:
        node = self.root_node
        for c in word:
            if c not in node.hashmap:
                node.hashmap[c] = self.Node()
            node = node.hashmap[c]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        root  = self.root_node

        def dfs(j, node):
            for idx in range(j, len(word)):
                c = word[idx]
                if c == ".":
                    for c_node in node.hashmap.values():
                        
                        if dfs(idx + 1, c_node):
                            return True
                    return False
                else:
                    if c not in node.hashmap:
                        return False
                    node = node.hashmap[c]

            return node.end_of_word

        return dfs(0, root)

