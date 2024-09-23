"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ln = len(s)
        ans1 = s[0]
        cur1 = 1
        for i in range(1, ln):
            le = r = i
            while True:
                if le > 0 and r < ln - 1 and s[le - 1] == s[r + 1]:
                    le -= 1
                    r += 1
                else:
                    break
            if cur1 < r - le + 1:
                cur1 = r - le + 1
                ans1 = s[le : r + 1]
        ans2 = ""
        cur2 = 0
        for i in range(1, ln):
            le = i - 1
            r = i
            if s[le] != s[r]:
                continue
            while True:
                if le > 0 and r < ln - 1 and s[le - 1] == s[r + 1]:
                    le -= 1
                    r += 1
                else:
                    break
            if cur2 < r - le + 1:
                cur2 = r - le + 1
                ans2 = s[le : r + 1]
        return ans1 if cur1 > cur2 else ans2
