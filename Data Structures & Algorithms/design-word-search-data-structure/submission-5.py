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
        node = root if root else self.root_node

        for idx, c in enumerate(word):
            if c == ".":
                print("hit a period")

                #rerun search but for every possible hash value in this current node
                for node in node.hashmap.values():            
                    if self.search(word[idx + 1:], node): #return characters after the "."
                        return True
                return False

            if c in node.hashmap:
                node = node.hashmap[c]
            else:
                return False
                
        return node.end_of_word
