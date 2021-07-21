# coding: utf-8

"""
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution(object):
    @staticmethod
    def two_sum(nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]
            lookup[num] = i
        return []


if __name__ == '__main__':
    su = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    so = Solution()
    n = so.two_sum(nums, target)
    print("结果: ", n)
