class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []

        word_char_frequency = Counter(words[0])

        for word in words:
            current_word_char_frequency = Counter(word)

            for c in word_char_frequency:
                word_char_frequency[c] = min(word_char_frequency[c], current_word_char_frequency[c])

        for c in word_char_frequency:
            for i in range(word_char_frequency[c]):
                result.append(c)

        return result
