"""
Title: Ransom Note

Given an arbitrary ransom note string and another string containing letters
from all the magazines, write a function that will return true if the ransom
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.


Example:
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote is not None and magazine is not None:
            ransomnote_char_frequency = {}
            magazine_char_frequency = {}

            for i in ransomNote:
                ransomnote_char_frequency[i] = ransomnote_char_frequency.get(i, 0) + 1
            for i in magazine:
                magazine_char_frequency[i] = magazine_char_frequency.get(i, 0) + 1

            for k, v in ransomnote_char_frequency.items():
                if k not in magazine_char_frequency or magazine_char_frequency[k] < v:
                    return False
            return True
        return False


def get_test_case_1() -> (str, str):
    return None, None


def get_test_case_2() -> (str, str):
    return None, ""


def get_test_case_3() -> (str, str):
    return "", None


def get_test_case_4() -> (str, str):
    return "", ""


def get_test_case_5() -> (str, str):
    return "a", "b"


def get_test_case_6() -> (str, str):
    return "aa", "ab"


def get_test_case_7() -> (str, str):
    return "aa", "aab"


if __name__ == "__main__":
    solution = Solution()

    #ransomNote, magazine = get_test_case_1()
    #ransomNote, magazine = get_test_case_2()
    #ransomNote, magazine = get_test_case_3()
    #ransomNote, magazine = get_test_case_4()
    #ransomNote, magazine = get_test_case_5()
    #ransomNote, magazine = get_test_case_6()
    ransomNote, magazine = get_test_case_7()
    print("\n ransomNote: ", ransomNote)
    print(" magazine: ", magazine)

    result = solution.canConstruct(ransomNote, magazine)
    print("\n result: ", result)
