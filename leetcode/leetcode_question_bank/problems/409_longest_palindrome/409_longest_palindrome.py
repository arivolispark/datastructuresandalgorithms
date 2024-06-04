class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = len(s)
        count = 0
        frequency_map = {}
        frequency_list = []
        odd_greater_than_one = False

        for i in range(length):
            frequency_map[s[i]] = frequency_map.get(s[i], 0) + 1

        if len(frequency_map.keys()) == 1:
            return length

        for k, v in frequency_map.items():
            frequency_list.append(v)

        frequency_list.sort(reverse=True)

        for i in range(len(frequency_list)):
            if frequency_list[i] % 2 == 0:
                count += frequency_list[i]
            elif frequency_list[i] > 1 and frequency_list[i] % 2 == 1:
                odd_greater_than_one = True
                count += (frequency_list[i] - 1)
            elif not odd_greater_than_one and frequency_list[i] == 1:
                count += 1
                break

        if odd_greater_than_one:
            count += 1

        return count
