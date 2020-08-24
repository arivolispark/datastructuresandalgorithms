"""
Title:  Stream of Characters

Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters
queried (in order from oldest to newest, including this letter just queried) spell
one of the words in the given list.


Example:
StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist



Note:
1) 1 <= words.length <= 2000
2) 1 <= words[i].length <= 2000
3) Words will only consist of lowercase English letters.
4) Queries will only consist of lowercase English letters.
5) The number of queries is at most 40000.

"""

from typing import List
from collections import deque


class Trie:

    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 26

    def insert(self, s):
        t = self
        for c in s:
            if t.children[ord(c) - ord('a')] is None:
                t.children[ord(c) - ord('a')] = Trie()
            t = t.children[ord(c) - ord('a')]
        t.endOfWord = True

    def search(self, s):
        t = self
        for c in s:
            if t.children[ord(c) - ord('a')] is None:
                return False
            t = t.children[ord(c) - ord('a')]
            if t.endOfWord:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = Trie()
        self.stream = deque()
        for w in words:
            self.t.insert(reversed(w))

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.t.search(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


def get_test_case_1():
    stream_checker = StreamChecker(["cd", "f", "kl"])  # init the dictionary.
    print(stream_checker.query('a'))  # return False
    print(stream_checker.query('b'))  # return False
    print(stream_checker.query('c'))  # return False
    print(stream_checker.query('d'))  # return True, because 'cd' is in the wordlist

    print(stream_checker.query('e'))  # return False
    print(stream_checker.query('f'))  # return True, because 'f' is in the wordlist

    print(stream_checker.query('g'))  # return False
    print(stream_checker.query('h'))  # return False
    print(stream_checker.query('i'))  # return False
    print(stream_checker.query('j'))  # return False
    print(stream_checker.query('k'))  # return False
    print(stream_checker.query('l'))  # return True, because 'kl' is in the wordlist


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    get_test_case_1()
