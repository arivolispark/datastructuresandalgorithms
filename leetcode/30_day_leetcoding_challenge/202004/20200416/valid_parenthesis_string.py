"""
Title:  Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', write
a function to check whether this string is valid.  We define the validity of
a string by these rules:

1) Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2) Any right parenthesis ')' must have a corresponding left parenthesis '('.
3) Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4) '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5) An empty string is also valid.


Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
1) The string size will be in the range [1, 100].

"""

from collections import deque


class Solution:

    def checkValidString(self, s: str) -> bool:
        if s is not None:
            n = len(s)
        if n == 0:
            return True
        else:
            validator_queue = deque()

            for i in range(n):
                if s[i] == ")":
                    if len(validator_queue) == 0:
                        return False
                    else:
                        if validator_queue[-1] == "(":
                            validator_queue.pop()
                        else:
                            validator_queue.append(s[i])
                else:
                    validator_queue.append(s[i])

            print("\n validator_queue: ", validator_queue)
            print(" len(validator_queue): ", len(validator_queue))

            size = len(validator_queue)
            if size == 0:
                return True
            else:
                count_left_parenthesis, count_right_parenthesis, count_star = 0, 0, 0
                result_queue = deque()

                for i in range(size):
                    if validator_queue[i] == "(":
                        if len(result_queue) == 0:
                            result_queue.append(validator_queue[i])
                            count_left_parenthesis += 1
                        elif count_left_parenthesis != count_right_parenthesis or count_left_parenthesis == count_right_parenthesis:
                            if count_star >= abs(count_left_parenthesis - count_right_parenthesis):
                                while len(result_queue) > 0:
                                    result_queue.pop()
                                count_left_parenthesis, count_right_parenthesis, count_star = 0, 0, 0
                                result_queue.append(validator_queue[i])
                                count_left_parenthesis += 1
                            elif count_right_parenthesis > count_left_parenthesis:
                                return False
                            else:
                                result_queue.append(validator_queue[i])
                                count_left_parenthesis += 1
                        else:
                            result_queue.append(validator_queue[i])
                            count_left_parenthesis += 1
                    elif validator_queue[i] == "*":
                        result_queue.append(validator_queue[i])
                        count_star += 1
                    else:
                        result_queue.append(validator_queue[i])
                        count_right_parenthesis += 1

                print("\n result_queue: ", result_queue)
                print(" len(result_queue): ", len(result_queue))
                print(" count_left_parenthesis: ", count_left_parenthesis)
                print(" count_star: ", count_star)
                print(" count_right_parenthesis: ", count_right_parenthesis)

                if len(result_queue) == 0:
                    return True
                elif count_left_parenthesis == count_right_parenthesis:
                    return True
                return count_star >= abs(count_left_parenthesis - count_right_parenthesis)


def get_test_case_1() -> str:
    return ""


def get_test_case_2() -> str:
    return "("


def get_test_case_3() -> str:
    return "*"


def get_test_case_4() -> str:
    return ")"


def get_test_case_5() -> str:
    return "(*"


def get_test_case_6() -> str:
    return "***("


def get_test_case_7() -> str:
    return "()"


def get_test_case_8() -> str:
    return "(*)"


def get_test_case_9() -> str:
    return "(*))"


def get_test_case_10() -> str:
    return "((*)"


def get_test_case_11() -> str:
    return "(((******))"


def get_test_case_12() -> str:
    # "(()) ( (()) ()() (*) (* () (())() ) () ) () () ( (()()) ((())) (*"
    return "(())((())()()(*)(*()(())())())()()((()())((()))(*"


def get_test_case_13() -> str:
    return "(())(())(((()*()()()))()((()()(*()())))(((*)()"


def get_test_case_14() -> str:
    return "(*())))()))))(()))))))(((())()())()*())))(((**)*()(()())(*)))(()*(*(())(())(()()())(()()*)((*()*))"


if __name__ == "__main__":
    solution = Solution()

    #s = get_test_case_1()
    #s = get_test_case_2()
    #s = get_test_case_3()
    #s = get_test_case_4()
    #s = get_test_case_5()
    #s = get_test_case_6()
    #s = get_test_case_7()
    #s = get_test_case_8()
    #s = get_test_case_9()
    #s = get_test_case_10()
    #s = get_test_case_11()
    #s = get_test_case_12()
    s = get_test_case_13()
    #s = get_test_case_14()

    print("\n s: ", s)
    print(" len(s: ", len(s))

    result = solution.checkValidString(s)
    print("\n result: ", result)
