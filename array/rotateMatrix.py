# -*- coding:utf-8 -*-

class Solution:
    def rotateMatrix(self, mat, n):
        # write code here
        res = [[0]*n for i in range(n)]

        for i in range(n):
            for j in range(n):
                res[j][n-1-i] = mat[i][j]

        return res

mat = [[1,2,3],[4,5,6],[7,8,9]]
n = 3
run = Solution()
res =  run.rotateMatrix(mat,n)
print (res)