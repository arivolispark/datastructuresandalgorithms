"""
Title:  Bulls and Cows

You are playing the following Bulls and Cows game with your friend: You write down a number
and ask your friend to guess what the number is. Each time your friend makes a guess, you
provide a hint that indicates how many digits in said guess match your secret number exactly
in both digit and position (called "bulls") and how many digits match the secret number but
locate in the wrong position (called "cows"). Your friend will use successive guesses and hints
to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to
indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.



Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.



Example 2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.


Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

"""


class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        char_frequency_map = {}
        bulls, cows = 0, 0

        bull_index = []

        if secret and guess:
            for i in range(len(secret)):
                if secret[i] == guess[i]:
                    bulls += 1
                    bull_index.append(i)
            #print(" bull_index: ", bull_index)

            modified_secret, modified_guess = "", ""
            for i in range(len(secret)):
                if i not in bull_index:
                    modified_secret = modified_secret + secret[i]

            for i in range(len(guess)):
                if i not in bull_index:
                    modified_guess = modified_guess + guess[i]

            #print(" modified_secret: ", modified_secret)
            #print(" modified_guess: ", modified_guess)

            for i in range(len(modified_secret)):
                char_frequency_map[modified_secret[i]] = char_frequency_map.get(modified_secret[i], 0) + 1
            #print(" char_frequency_map: ", char_frequency_map)

            for i in range(len(modified_guess)):
                if modified_guess[i] in char_frequency_map:
                    cows += 1
                    char_frequency_map[modified_guess[i]] -= 1
                    if char_frequency_map[modified_guess[i]] == 0:
                        del char_frequency_map[modified_guess[i]]

        result = str(bulls) + "A" + str(cows) + "B"
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.getHint("1807", "7810"), "1A3B")
    test(solution.getHint("1123", "0111"), "1A1B")
