"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/container-with-most-water
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        ll = 0
        r = len(height) - 1
        ans = 0
        while ll < r:
            ans = max(ans, min(height[ll], height[r]) * (r - ll))
            if height[ll] < height[r]:
                ll += 1
            else:
                r -= 1
        return ans
