"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/word-break/
"""


def f(s, cur, dct, memo):
    if cur in memo:
        return memo[cur]
    if cur == s:
        return True
    if len(cur) >= len(s) or cur != s[: len(cur)]:
        return False
    if s[len(cur)] in dct:
        for i in dct[s[len(cur)]]:
            if f(s, cur + i, dct, memo):
                memo[cur] = True
                return True
    memo[cur] = False
    return False


class Solution:

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        se = set(s)
        see = set("".join(wordDict))
        if not se.issubset(see):
            return False
        dct = {}
        for word in wordDict:
            if word[0] not in dct:
                dct[word[0]] = []
            dct[word[0]].append(word)
        memo = {}
        return f(s, "", dct, memo)
