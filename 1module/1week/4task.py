"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description
"""

dct = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def f(inp, s, cur, mas):
    if len(inp) == cur:
        if cur == 0:
            return
        mas.append(s)
        return
    for j in dct[inp[cur]]:
        f(inp, s + j, cur + 1, mas)


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        ans = []
        f(digits, "", 0, ans)
        return ans
