class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

    def insert(self, word):
        node = self
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
            node.count += 1

    def search(self, word):
        node = self
        total_count = 0
        for char in word:
            index = ord(char) - ord('a')
            if node.children[index] is None:
                return total_count
            node = node.children[index]
            total_count += node.count
        return total_count


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:        
        trie = Trie()
        for word in words:
            trie.insert(word)
        return [trie.search(word) for word in words]
