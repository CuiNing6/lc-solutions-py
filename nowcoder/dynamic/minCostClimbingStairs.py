#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param cost int整型一维数组
# @return int整型
#
class Solution:
    def minCostClimbingStairs(self , cost ):
        # write code here
        n = len(cost)

        dp = [0] * (n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n+1):
            if i == n:
                dp[i] = min(dp[i-1], dp[i-2])
            else:
                dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return dp[n]

cost = [1,100,1,1,1,90,1,1,80,1]

r = Solution()
res = r.minCostClimbingStairs(cost)
print(res)
