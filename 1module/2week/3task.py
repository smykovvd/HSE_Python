"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/generate-parentheses
"""


def f(s):
    if len(s) == 1:
        return "1" + s
    ss = ""
    cou = 1
    last = s[0]
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            ss += str(cou) + last
            cou = 1
            last = s[i + 1]
        else:
            cou += 1

    return ss + str(cou) + s[-1]


class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(1, n):
            s = f(s)
        return s
