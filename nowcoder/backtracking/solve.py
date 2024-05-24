#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 判断岛屿数量
# @param grid char字符型二维数组
# @return int整型
#

# 描述
# 给一个01矩阵，1代表是陆地，0代表海洋， 如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。
# 岛屿: 相邻陆地可以组成一个岛屿（相邻:上下左右） 判断岛屿个数。


class Solution:
    def solve(self , grid ):
        # write code here
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])
        res = 0

        def dfs(grid, row, col, i, j):
            if i < 0 or j < 0 or i > row-1 or j > col-1 or grid[i][j] != 1:
                return

            grid[i][j] = 2

            dfs(grid, row, col, i - 1, j)
            dfs(grid, row, col, i + 1, j)
            dfs(grid, row, col, i, j - 1)
            dfs(grid, row, col, i, j + 1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    res += 1
                    dfs(grid, row, col, i, j)

        return res

grid = [[1,1,0,0,0],[0,1,0,1,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,1,1,1]]

r = Solution()
res = r.solve(grid)
print(res)