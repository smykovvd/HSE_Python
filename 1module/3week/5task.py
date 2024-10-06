"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/next-permutation
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        ll = i + 1
        r = len(nums) - 1
        while ll < r:
            nums[ll], nums[r] = nums[r], nums[ll]
            ll += 1
            r -= 1
