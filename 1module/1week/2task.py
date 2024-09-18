"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description/
"""


def longestPalindrome(self, s: str) -> str:
    ln = len(s)
    ans1 = s[0]
    cur1 = 1
    for i in range(1, ln):
        l = r = i
        while True:
            if l > 0 and r < ln - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            else:
                break
        if cur1 < r - l + 1:
            cur1 = r - l + 1
            ans1 = s[l : r + 1]

    ans2 = ""
    cur2 = 0
    for i in range(1, ln):
        l = i - 1
        r = i
        if s[l] != s[r]:
            continue
        while True:
            if l > 0 and r < ln - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
            else:
                break
        if cur2 < r - l + 1:
            cur2 = r - l + 1
            ans2 = s[l : r + 1]
    return ans1 if cur1 > cur2 else ans2


print(longestPalindrome(1, "cbbd"))
