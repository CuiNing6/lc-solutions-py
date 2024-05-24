#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def rob(self , nums ):
        # write code here
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[-1]

        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]


        for i in range(2,len(nums)+1):
            dp[i] = max(nums[i-1]+dp[i-2],dp[i-1])

        return dp[len(nums)]


    def rob_v1(self , nums ):
        # write code here
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[-1]

        #偷第一家
        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]

        for i in range(2,len(nums)):
            dp[i] = max(nums[i-1]+dp[i-2],dp[i-1])

        #不偷第一家
        dp1 = [0]*(len(nums)+1)
        dp1[1] = 0

        for i in range(2,len(nums)+1):
            dp1[i] = max(nums[i-1]+dp1[i-2],dp1[i-1])

        return max(dp[len(nums)-1],dp1[len(nums)])


nums = [9,10]
r = Solution()
res = r.rob_v1(nums)
print(res)