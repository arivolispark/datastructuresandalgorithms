from collections import deque


class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        return get_editted_string(S) == get_editted_string(T)


def get_editted_string(S: str) -> str:
    q = deque()

    for chr in S:
        if chr != "#":
            q.append(chr)
        else:
            if len(q) > 0:
                q.pop()
    return ''.join(list(q))


if __name__ == "__main__":
    solution = Solution()

    #s1 = "ab#c"
    #s1 = "ab##"
    #s1 = "a##c"
    s1 = "a#c"
    print("\n s1: ", s1)

    #s2 = "ad#c"
    #s2 = "c#d#"
    #s2 = "#a#c"
    s2 = "b"
    print(" s2: ", s2)

    result = solution.backspaceCompare(s1, s2)
    print("\n result: ", result)
