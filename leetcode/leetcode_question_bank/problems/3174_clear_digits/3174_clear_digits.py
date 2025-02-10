class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if (ord(s[i]) >= 48 and ord(s[i]) <= 57) and len(stack) > 0:
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)
