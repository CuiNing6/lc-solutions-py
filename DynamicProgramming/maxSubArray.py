# -*- coding:UTF-8 -*-
'''
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

分析: 利用动态规划的思路解题: 首先寻找最优子问题,[-2,1,-3,4,-1,2,1,-5,4],第一个最优子问题为-2,那么到下一个1时,其最优为当前值或者当前值加上上一个最优值,因而可以得到其递推公式.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[-1]

        mxlen = len(nums)
        dp = [0 for i in range(mxlen)]
        dp[0] = nums[0]

        for i in range(1,len(nums)):
            tmp = dp[i-1] + nums[i]
            dp[i] = max(dp[i], tmp)

        return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]

run = Solution()
res =  run.maxSubArray(nums)
print (res)