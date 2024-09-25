"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/generate-parentheses
"""


def f(cur, op, cl, n, ans):
    if op:
        if op < n:
            f(cur + "(", op + 1, cl, n, ans)
            if op > cl:
                f(cur + ")", op, cl + 1, n, ans)
        elif cl < n:
            f(cur + ")", op, cl + 1, n, ans)
        else:
            ans.append(cur)
            return
    else:
        f(cur + "(", op + 1, cl, n, ans)


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        f("", 0, 0, n, ans)
        return ans
