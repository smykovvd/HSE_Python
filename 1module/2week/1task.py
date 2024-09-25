"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        cur = ""
        s = s.strip()
        if s == "":
            return 0
        if s[0] == "-":
            cur += "-"
            for i in range(1, len(s)):
                if s[i] in "0123456789":
                    cur += s[i]
                else:
                    break
            cur = list(cur)
            while len(cur) > 2 and cur[1] == "0":
                cur.pop(1)
            cur = "".join(cur)

            if cur in "- ":
                return 0
            cur = int(cur)
            if cur < -(2**31):
                return -(2**31)
            return cur
        else:
            start = 0
            if s[0] == "+":
                start += 1
            for i in range(start, len(s)):
                if s[i] in "0123456789":
                    cur += s[i]
                else:
                    break
            cur = list(cur)
            while len(cur) > 1 and cur[0] == "0":
                cur.pop(0)
            cur = "".join(cur)
            if cur in "- ":
                return 0
            cur = int(cur)
            if cur > 2**31 - 1:
                return 2**31 - 1
            return cur
