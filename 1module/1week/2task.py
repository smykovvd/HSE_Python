"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description/
"""


def longestPalindrome(self, s: str) -> str:
    ln = len(s)
    ans1 = s[0]
    cur1 = 1
    for i in range(1, ln):
        l1 = i
        r1 = i
        while True:
            if l1 > 0 and r1 < ln - 1 and s[l1 - 1] == s[r1 + 1]:
                l1 -= 1
                r1 += 1
            else:
                break
        if cur1 < r1 - l1 + 1:
            cur1 = r1 - l1 + 1
            ans1 = s[l1: r1 + 1]

    ans2 = ""
    cur2 = 0
    for i in range(1, ln):
        l2 = i - 1
        r2 = i
        if s[l2] != s[r2]:
            continue
        while True:
            if l2 > 0 and r2 < ln - 1 and s[l2 - 1] == s[r2 + 1]:
                l2 -= 1
                r2 += 1
            else:
                break
        if cur2 < r2 - l2 + 1:
            cur2 = r2 - l2 + 1
            ans2 = s[l2: r2 + 1]
    return ans1 if cur1 > cur2 else ans2


print(longestPalindrome(1, "cbbd"))
