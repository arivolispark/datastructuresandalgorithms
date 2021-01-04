class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if s:
            char_freq_map = {}
            number_of_odd_chars = 0
            for i in range(len(s)):
                char_freq_map[s[i]] = char_freq_map.get(s[i], 0) + 1

            for k, v in char_freq_map.items():
                if v % 2 == 1:
                    number_of_odd_chars += 1
                    if number_of_odd_chars > 1:
                        return False

            return True
