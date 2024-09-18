"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = 0
        ans = 0
        temp = []
        lnt = 0
        while r < len(s):
            if s[r] in temp:
                ans = max(ans, lnt)
                if s[l] == s[r]:
                    l += 1
                    temp.pop(0)
                    lnt -= 1
                else:
                    while s[l] != s[r]:
                        l += 1
                        temp.pop(0)
                        lnt -= 1
                        if s[l] == s[r]:
                            temp.pop(0)
                            lnt -= 1
                            l += 1
                            break

            temp += [s[r]]
            lnt += 1
            ans = max(ans, lnt)
            r += 1
        return ans
