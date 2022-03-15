class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isEnd = False
class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        curr = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            if not curr.children[index]:
                curr.children[index] = self.getNode()
            curr = curr.children[index]
        curr.isEnd = True

    def search(self, key):
        curr = self.root
        for level in range(len(key)):
            index = self._charToIndex(key[level])
            if not curr.children[index]:
                return False
            curr = curr.children[index]
 
        return curr.isEnd
