class PrefixTree:

    class Node:
        def __init__(self):
            self.arr = [] 
            self.hashmap = {}
            self.end_of_word = False

    def __init__(self):
        self.root_node = self.Node()

    def insert(self, word: str) -> None:
        node = self.root_node
        for idx, c in enumerate(word):
            if c not in node.hashmap:
                node.hashmap[c] = self.Node()
            node = node.hashmap[c]  # move into the node for that character
            
            # if last character in the word mark it as end of word
            if idx == len(word) - 1:
                node.end_of_word = True
                
            print(node.hashmap)
            print(c)

    def search(self, word: str) -> bool:
        #start at root
        node = self.root_node
        for idx, c in enumerate(word):
            if c in node.hashmap:
                if node.hashmap[c].end_of_word and idx == len(word) - 1:
                    return True
                node = node.hashmap[c]
            else:
                return False
        return False

    def startsWith(self, prefix: str) -> bool:
        #start at root
        node = self.root_node
        for idx, c in enumerate(prefix):
            if c in node.hashmap:
                node = node.hashmap[c]
                if idx == len(prefix) - 1:
                    return True
            else:
                return False
        return False
        