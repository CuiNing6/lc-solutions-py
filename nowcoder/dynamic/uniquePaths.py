#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param m int整型
# @param n int整型
# @return int整型
#
class Solution:
    def uniquePaths(self , m , n ):
        # write code here

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if j == 1:
                    dp[i][j] = 1
                    continue
                if i == 1:
                    dp[i][j] = 1
                    continue

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m][n]


m = 3
n = 3
r = Solution()
res = r.uniquePaths(m,n)
print(res)




