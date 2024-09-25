"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/zigzag-conversion/
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        ln = len(s)
        m = 0
        while ln > 0:
            ln -= numRows
            m += 1
            if ln <= 0:
                break
            m += numRows
            ln -= numRows
            if numRows > 2:
                m -= 2
                ln += 2

        mas = {x: [] for x in range(numRows)}

        cur = 0
        i = j = 0
        while cur != len(s):
            while j < numRows and cur != len(s):
                mas[j] += [cur]
                j += 1
                cur += 1
            i += 1
            while j > 0 and j > numRows - 2:
                j -= 1
            while j > 0 and cur != len(s):
                mas[j] += [cur]
                i += 1
                j -= 1
                cur += 1
        ans = ""
        for i in range(numRows):
            for j in mas[i]:
                ans += s[j]
        return ans
