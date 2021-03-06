"""
Title:  Goat Latin

A sentence S is given, composed of words separated by spaces. Each word consists
of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar
to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and
append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting
with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added
to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.



Example 1:
Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"



Example 2:
Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


Notes:
1) S contains only uppercase, lowercase and spaces. Exactly one space between each word.
2) 1 <= S.length <= 150.

"""


class Solution:

    def toGoatLatin(self, S: str) -> str:
        result = ''
        if S:
            vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

            wordlist = S.split(" ")
            wordlist_len = len(wordlist)

            for i in range(wordlist_len):
                if wordlist[i][0] not in vowels:
                    wordlist[i] = wordlist[i][1:] + wordlist[i][0]
                wordlist[i] += "ma"

                wordlist[i] += (i + 1) * 'a'

                result += wordlist[i]
                if i < wordlist_len - 1:
                    result += ' '

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.toGoatLatin("I speak Goat Latin"), "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
    test(solution.toGoatLatin("The quick brown fox jumped over the lazy dog"), "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
    test(solution.toGoatLatin("Each word consists of lowercase and uppercase letters only"), "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa")

