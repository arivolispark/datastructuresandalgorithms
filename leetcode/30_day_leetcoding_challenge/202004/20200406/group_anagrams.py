"""
Title:  Group Anagrams

Given an array of strings, group anagrams together.


Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]


Note:
    1) All inputs will be in lowercase.
    2) The order of your output does not matter.


Time:  O(N)
Space:  O(N)
"""

from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_group_map = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in anagram_group_map:
                anagram_group_map[sorted_word] = [word]
            else:
                anagram_group_map[sorted_word].append(word)

        for anagrams_list in anagram_group_map.values():
            result.append(anagrams_list)

        return result


if __name__ == "__main__":
    #strs = []
    #strs = ["eat"]
    #strs = ["eat", "bat"]
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("\n strs: ", strs)

    solution = Solution()
    result = solution.groupAnagrams(strs)
    print("\n result: ", result)
