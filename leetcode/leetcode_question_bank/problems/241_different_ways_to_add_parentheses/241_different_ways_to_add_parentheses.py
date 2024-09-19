class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        result = []
        for i in range(len(expression)):
            if expression[i] in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if expression[i] == '+':
                            result.append(l+r)
                        elif expression[i] == '-':
                            result.append(l-r)
                        elif expression[i] == '*':
                            result.append(l*r)
        return result
