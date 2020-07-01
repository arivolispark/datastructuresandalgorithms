"""
Title:  Word Search II

Given a 2D board and a list of words from the dictionary, find all
words in the board.

Each word must be constructed from letters of sequentially adjacent
cell, where "adjacent" cells are those horizontally or vertically
neighboring. The same letter cell may not be used more than once in a word.


Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Note:
1) All inputs are consist of lowercase letters a-z.
2) The values of words are distinct.

"""

from typing import List


class Trie:

    def __init__(self):
        self.end_of_word = False
        self.children = [None] * 26

    def insert(self, word):
        curr = self

        for chr in word:
            idx = ord(chr) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Trie()
            curr = curr.children[idx]

        curr.end_of_word = True


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) == 0:
            return []

        trie = Trie()
        for w in words:
            trie.insert(w)

        word_set = set()
        self.board = board
        self.result = word_set

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, trie, "")

        word_list = list(word_set)
        return word_list

    def dfs(self, i, j, trie, s):
        chr = self.board[i][j]

        if chr == '$':
            return

        self.board[i][j] = '$'

        tr = trie.children[ord(chr) - ord('a')]
        if tr is not None:
            ss = s + chr
            if tr.end_of_word:
                self.result.add(ss)
            if i < len(self.board) - 1:
                self.dfs(i + 1, j, tr, ss)
            if j < len(self.board[0]) - 1:
                self.dfs(i, j + 1, tr, ss)
            if i > 0:
                self.dfs(i - 1, j, tr, ss)
            if j > 0:
                self.dfs(i, j - 1, tr, ss)
                
        self.board[i][j] = chr


def get_test_case_1():
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    return board, words


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    board, words = get_test_case_1()

    test(solution.findWords(board, words), ["eat","oath"])
