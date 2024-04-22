class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        unique_letters = set()
        special_chars_map = {}

        if word:
            for i in range(len(word)):
                unique_letters.add(word[i])

            for i in unique_letters:
                if ord(i) >= 97 and ord(i) <= 122:
                    if i not in special_chars_map:
                        special_chars_map[i] = i
            
            for i in unique_letters:
                if ord(i) >= 65 and ord(i) <= 90:
                    if chr(ord(i) + 32) in special_chars_map:
                        count += 1

        return count
