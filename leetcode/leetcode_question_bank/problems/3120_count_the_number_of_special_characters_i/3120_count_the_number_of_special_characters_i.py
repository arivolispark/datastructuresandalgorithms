class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        special_chars_map = {}

        if word:
            for i in range(len(word)):
                if word[i] not in special_chars_map:
                    special_chars_map[word[i]] = word[i]

            for c in special_chars_map.keys():
                if ord(c) >= 97 and ord(c) <= 122:
                    if chr(ord(c) - 32) in special_chars_map:
                        count += 1

        return count
