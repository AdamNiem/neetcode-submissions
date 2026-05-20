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

    def search(self, word: str, root: Node = None) -> bool:
        node  = root if root else self.root_node

        for idx, c in enumerate(word):
            if c == ".":
                for c_node in node.hashmap.values():
                    word_to_search = word[idx + 1:]
                    if self.search(word_to_search, c_node):
                        return True
                return False
            else:
                if c not in node.hashmap:
                    return False
                node = node.hashmap[c]

        return node.end_of_word

