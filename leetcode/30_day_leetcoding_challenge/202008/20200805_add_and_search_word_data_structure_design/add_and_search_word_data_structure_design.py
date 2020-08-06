"""
Title:  Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)


search(word) can search a literal word or a regular expression
string containing only letters a-z or .. A . means it can represent
any one letter.


Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true


Note:
1) You may assume that all words are consist of lowercase letters a-z.


"""


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self
        for c in word:
            if curr.children[ord(c) - ord('a')] is None:
                curr.children[ord(c) - ord('a')] = WordDictionary()
            curr = curr.children[ord(c) - ord('a')]

        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch is not None and ch.search(word[i + 1:]):
                        return True
                return False

            if curr.children[ord(c) - ord('a')] is None:
                return False
            curr = curr.children[ord(c) - ord('a')]

        return curr is not None and curr.isEndOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


def get_test_case_1():
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad")) # -> false
    print(wordDictionary.search("bad")) # -> true
    print(wordDictionary.search(".ad")) # -> true
    print(wordDictionary.search("b..")) # -> true


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    get_test_case_1()
