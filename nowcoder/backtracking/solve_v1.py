#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 递增路径的最大长度
# @param matrix int整型二维数组 描述矩阵的每个数
# @return int整型
#

# 描述
# 给定一个 n 行 m 列矩阵 matrix ，矩阵内所有数均为非负整数。
# 你需要在矩阵中找到一条最长路径，使这条路径上的元素是递增的。并输出这条最长路径的长度。


class Solution:
    def solve(self , matrix ):
        # write code here
        if not matrix:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        dp = [[0 for m in range(col)] for n in range(row)]

        res = 0

        def dfs(matrix,row,col,i,j,dp):
            if dp[i][j] != 0:
                return dp[i][j]

            dp[i][j] += 1

            if i-1>=0 and i-1<row and j>=0 and j<col and matrix[i-1][j] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(matrix,row,col,i-1,j,dp)+1)
            if i+1>=0 and i+1<row and j>=0 and j<col and matrix[i+1][j] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(matrix, row, col, i+1, j, dp) + 1)
            if i>=0 and i<row and j-1>=0 and j-1<col and matrix[i][j-1] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(matrix, row, col, i, j-1, dp) + 1)
            if i>=0 and i<row and j+1>=0 and j+1<col and matrix[i][j+1] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(matrix, row, col, i, j+1, dp) + 1)

            return dp[i][j]


        for i in range(row):
            for j in range(col):
                res = max(res,dfs(matrix,row,col,i,j,dp))

        return res


matrix = [[1,2,3],[4,5,6],[7,8,9]]
r = Solution()
res = r.solve(matrix)
print(res)
