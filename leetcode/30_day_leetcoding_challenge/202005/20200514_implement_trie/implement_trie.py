"""
Title:  Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.


Example:
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true


Note:
1) You may assume that all inputs are consist of lowercase letters a-z.
2) All inputs are guaranteed to be non-empty strings.

"""


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.children = {}
        self.word_ends_here = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        parent = self.root
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TreeNode(char)
            parent = parent.children[char]
            if i == len(word) - 1:
                parent.word_ends_here = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        parent = self.root
        for char in word:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return parent.word_ends_here

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        parent = self.root
        for char in prefix:
            if char not in parent.children:
                return False
            parent = parent.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    trie = Trie()

    test(trie.insert("apple"), None)
    test(trie.search("apple"), True)
    test(trie.search("app"), False)
    test(trie.startsWith("app"), True)
    test(trie.insert("app"), None)
    test(trie.search("app"), True)
