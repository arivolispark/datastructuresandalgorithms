class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = []
        if word and ch:
            position = word.find(ch)
            if position == -1:
                return word
            else:
                for i in range(position, -1, -1):
                    result.append(word[i])
                for i in range(position+1, len(word), 1):
                    result.append(word[i])
        return ''.join(result)
