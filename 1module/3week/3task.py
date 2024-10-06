"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/3sum-closest
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        n = len(nums)
        closest = 5000000
        for i in range(n):
            ll = i + 1
            r = n - 1
            while ll < r:
                s = nums[i] + nums[ll] + nums[r]
                if abs(target - s) < abs(target - closest):
                    closest = s
                if s < target:
                    ll += 1
                else:
                    r -= 1
        return closest
