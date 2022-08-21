# -*- coding:UTF-8 -*-

# 一个整数矩阵，输出c最长严格的递增路径的长度。
# 每个单元格，可以往上，下，左，右四个方向移动。 不能在对角线方向上移动或移动到边界外（即不允许环绕）。
# 示例 1:
# 输入: nums = [ [9,9,4], [6,6,8], [2,1,1] ] 输出: 4 解释: 最长递增路径为 [1, 2, 6, 9]。 示例 2:
# 输入: nums = [ [3,4,5], [3,2,6], [2,2,1] ] 输出: 4 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。



def test(nums):
    if nums is None:
        return None

    m = len(nums)
    n = len(nums[0])

    res = 0

    tmp = [[0 for i in range(n)] for j in range(m)]

    dir = [(-1,0),(1,0),(0,1),(0,-1)]

    def dfs(i,j):
        tmp_res = 1

        for dx, dy in dir:
            x = i + dx
            y = j + dy

            if x >= 0 and x < m and y >= 0 and y < n and nums[x][y] > nums[i][j]:
                tmp_res = max(tmp_res, tmp[x][y]+1) if tmp[x][y] else max(tmp_res, dfs(x,y)+1)

            tmp[i][j] = tmp_res

        return tmp_res

    for i in range(m):
        for j in range(n):
            if tmp[i][j]:
                res = max(res,tmp[i][j])
            else:
                res = max(res,dfs(i,j))

    return res

