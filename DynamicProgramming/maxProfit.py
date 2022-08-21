# -*- coding:UTF-8 -*-
'''
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

思路：动态规划，设置一个变量记录买入的最小金额
[7,1,5,3,6,4] 从最后一个4开始分析，比如我从4卖出，那么其获得的最大利润为（6）的时候最大利润与（4）-最小值之间的最大值，递推式为  f（4）=max（f（6），4-最小金额） 边界： f（0）=0，最优子结构：f（4）的最有子结构为f（6）
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        dp = [0 for i in range(len(prices))]
        min_prices = prices[0]

        for i in range(1, len(prices)):
            tmp = prices[i] - min_prices
            dp[i] = max(tmp, dp[i-1])

            if prices[i] < min_prices:
                min_prices = prices[i]

        return max(dp)

    def maxProfit_v1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :无限次
        """
        if len(prices) <= 1:
            return 0

        dp = [0 for i in range(len(prices))]

        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            dp[i] = max(0, tmp)

        return sum(dp)

    def maxProfit_v2(self, prices,k):
        """
        :type prices: List[int]
        :rtype: int
        :k次
        """
        if len(prices) <= 1:
            return 0

        dp = [[[0]*2 for i in range(k+1)] for i in range(len(prices))]

        for j in range(k+1):
            dp[0][j][1] = -prices[0]

        for i in range(1,len(prices)):
            for j in range(1,k+1):
                dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])

        return dp[-1][-1][0]


prices = [7,1,5,3,6,4]
prices1 = [7,6,4,3,1]
prices2 = [1,8,2,7,3,6,4,5]
prices3 = [3,3,5,0,0,3,1,4]
run = Solution()
res =  run.maxProfit(prices2)
res_v1 =  run.maxProfit_v1(prices2)
res_v2 =  run.maxProfit_v2(prices2,2)
print (res_v2)