"""
Title:  648. Replace Words

In English, we have a concept called root, which can be followed by some other
word to form another longer word - let's call this word derivative. For example, when
the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated
by spaces, replace all the derivatives in the sentence with the root forming it. If a
derivative can be replaced by more than one root, replace it with the root that has the
shortest length.

Return the sentence after the replacement.



Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"


Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"


Constraints:
1) 1 <= dictionary.length <= 1000
2) 1 <= dictionary[i].length <= 100
3) dictionary[i] consists of only lower-case letters.
4) 1 <= sentence.length <= 106
5) sentence consists of only lower-case letters and spaces.
6) The number of words in sentence is in the range [1, 1000]
7) The length of each word in sentence is in the range [1, 1000]
8) Every two consecutive words in sentence will be separated by exactly one space.
9) sentence does not have leading or trailing spaces.

"""

from typing import List


class Node:
    def __init__(self):
        self.edges = {}
        self.end_of_word = False


class Trie:
    def __init__(self, dictionary):
        self.root = Node()

        for word in dictionary:
            self.add(word)

    def add(self, word):
        node = self.root

        for c in word:
            if c not in node.edges:
                node.edges[c] = Node()
            node = node.edges[c]
        node.end_of_word = True

    def search_prefix(self, word):
        result = []

        node = self.root

        for c in word:
            if c not in node.edges:
                return word

            result.append(c)

            node = node.edges[c]
            if node.end_of_word:
                return "".join(result)

        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        result = []

        t = Trie(dictionary)

        words = sentence.split()
        for word in words:
            result.append(t.search_prefix(word))

        return " ".join(result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"), "the cat was rat by the bat")
    test(solution.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"), "a a b c")
    test(solution.replaceWords(["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"), "a a a a a a a a bbb baba a")
    test(solution.replaceWords(["catt","cat","bat","rat"], "the cattle was rattled by the battery"), "the cat was rat by the bat")
    test(solution.replaceWords(["e","k","c","harqp","h","gsafc","vn","lqp","soy","mr","x","iitgm","sb","oo","spj","gwmly","iu","z","f","ha","vds","v","vpx","fir","t","xo","apifm","tlznm","kkv","nxyud","j","qp","omn","zoxp","mutu","i","nxth","dwuer","sadl","pv","w","mding","mubem","xsmwc","vl","farov","twfmq","ljhmr","q","bbzs","kd","kwc","a","buq","sm","yi","nypa","xwz","si","amqx","iy","eb","qvgt","twy","rf","dc","utt","mxjfu","hm","trz","lzh","lref","qbx","fmemr","gil","go","qggh","uud","trnhf","gels","dfdq","qzkx","qxw"], "ikkbp miszkays wqjferqoxjwvbieyk gvcfldkiavww vhokchxz dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dco kddxmckhvqifbuzkhstp wc ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy ifvifheoxqlbosfww mengfdydekwttkhbzenk wjhmmyltmeufqvcpcxg hthcuovils ldipovluo aiprogn nusquzpmnogtjkklfhta klxvvlvyh nxzgnrveghc mpppfhzjkbucv cqcft uwmahhqradjtf iaaasabqqzmbcig zcpvpyypsmodtoiif qjuiqtfhzcpnmtk yzfragcextvx ivnvgkaqs iplazv jurtsyh gzixfeugj rnukjgtjpim hscyhgoru aledyrmzwhsz xbahcwfwm hzd ygelddphxnbh rvjxtlqfnlmwdoezh zawfkko iwhkcddxgpqtdrjrcv bbfj mhs nenrqfkbf spfpazr wrkjiwyf cw dtd cqibzmuuhukwylrnld dtaxhddidfwqs bgnnoxgyynol hg dijhrrpnwjlju muzzrrsypzgwvblf zbugltrnyzbg hktdviastoireyiqf qvufxgcixvhrjqtna ipfzhuvgo daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh qzsaobsghgm ichlpsjlsrwzhbyfhm ksenb bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn frotscysdyclrc ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp"), "i miszkays w gvcfldkiavww v dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dc k w ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy i mengfdydekwttkhbzenk w h ldipovluo a nusquzpmnogtjkklfhta k nxzgnrveghc mpppfhzjkbucv c uwmahhqradjtf i z q yzfragcextvx i i j gzixfeugj rnukjgtjpim h a x h ygelddphxnbh rvjxtlqfnlmwdoezh z i bbfj mhs nenrqfkbf spfpazr w c dtd c dtaxhddidfwqs bgnnoxgyynol h dijhrrpnwjlju muzzrrsypzgwvblf z h q i daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh q i k bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala q gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn f c pxbd oklwhcppuziixpvihihp")
