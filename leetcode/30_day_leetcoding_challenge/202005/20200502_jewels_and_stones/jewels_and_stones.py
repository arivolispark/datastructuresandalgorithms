"""
Title: Jewels and Stones

You're given strings J representing the types of stones that are
jewels, and S representing the stones you have.  Each character
in S is a type of stone you have.  You want to know how many of
the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters
in J and S are letters. Letters are case sensitive, so "a" is
considered a different type of stone from "A".


Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3


Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Note:
1) S and J will consist of letters and have length at most 50.
2) The characters in J are distinct.
"""


class Solution:

    def numJewelsInStones(self, J: str, S: str) -> int:
        number_of_jewels = 0
        if J and S:
            jewel_set = set()
            stone_freq_map = {}

            for i in range(len(J)):
                jewel_set.add(J[i])

            for i in range(len(S)):
                if S[i] in jewel_set:
                    stone_freq_map[S[i]] = stone_freq_map.get(S[i], 0) + 1

            #print("\n jewel_set: ", jewel_set)
            #print(" stone_freq_map: ", stone_freq_map)

            for k, v in stone_freq_map.items():
                if k in jewel_set:
                    number_of_jewels += v
        return number_of_jewels


def get_test_case_1() -> (str, str):
    return None, None


def get_test_case_2() -> (str, str):
    return None, ""


def get_test_case_3() -> (str, str):
    return "", None


def get_test_case_4() -> (str, str):
    return "", ""


def get_test_case_5() -> (str, str):
    return "aA", "aAAbbbb"


def get_test_case_6() -> (str, str):
    return "z", "ZZ"


if __name__ == "__main__":
    solution = Solution()

    #J, S = get_test_case_1()
    #J, S = get_test_case_2()
    #J, S = get_test_case_3()
    #J, S = get_test_case_4()
    J, S = get_test_case_5()
    #J, S = get_test_case_6()
    print("\n J: ", J)
    print(" S: ", S)

    number_of_jewels = solution.numJewelsInStones(J, S)
    print("\n number_of_jewels: ", number_of_jewels)
