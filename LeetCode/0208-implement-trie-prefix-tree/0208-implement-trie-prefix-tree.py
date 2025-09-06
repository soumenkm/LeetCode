class Node:
    def __init__(self):
        self.alpha = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.alpha:
                node.alpha[char] = Node()
            node = node.alpha[char]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.alpha:
                return False
            node = node.alpha[char]
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.alpha:
                return False
            node = node.alpha[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)