"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/integer-to-roman
"""

dct = {0: "", 1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}


class Solution:
    def intToRoman(self, num: int) -> str:
        ln = len(str(num))
        ans = ""
        for i in range(ln):
            cur = int(str(num)[i])
            if cur <= 3:
                ans += cur * dct[10 ** (ln - i - 1)]
            elif cur == 4:
                ans += dct[10 ** (ln - i - 1)] + dct[5 * 10 ** (ln - i - 1)]
            elif cur == 5:
                ans += dct[5 * 10 ** (ln - i - 1)]
            elif cur == 9:
                ans += dct[10 ** (ln - i - 1)] + dct[10 ** (ln - i)]
            else:
                ans += dct[5 * 10 ** (ln - i - 1)] + (cur - 5) * dct[10 ** (ln - i - 1)]
        return ans
