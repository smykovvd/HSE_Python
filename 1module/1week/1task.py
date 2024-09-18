"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-valid-parentheses/description/
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ln = len(s)
        mas = ["0"] * ln
        cur = []
        for i in range(ln):
            a = s[i]
            if a == "(":
                cur += [i]
            else:
                if len(cur) != 0:
                    mas[cur.pop()] = "1"
                    mas[i] = "1"
        return max(map(len, "".join(mas).split("0")))
