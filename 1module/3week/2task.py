"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/4sum/
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c, d = b + 1, n - 1
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    if s == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1
                    elif s < target:
                        c += 1
                    else:
                        d -= 1
        return ans
