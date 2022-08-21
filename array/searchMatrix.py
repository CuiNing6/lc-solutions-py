# -*- coding:UTF-8 -*-
'''
矩阵查找

描述
请写出一个高效的在m*n矩阵中判断目标值是否存在的算法，矩阵具有如下特征：
每一行的数字都从左到右排序
每一行的第一个数字都比上一行最后一个数字大
例如：
对于下面的矩阵：
[
    [1,   3,  5,  9],
    [10, 11, 12, 30],
    [230, 300, 350, 500]
]
要搜索的目标值为3，返回true；

输入：[[1,3,5,9],[10,11,12,30],[230, 300, 350, 500]],3
返回值：true
'''
class Solution:
    def searchMatrix(self , matrix , target ):
        # write code here
        n,m = len(matrix), len(matrix[0])
        i = 0
        j = m-1

        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i = i + 1
            else:
                j = j - 1

        return False



matrix = [[1,3,5,9],[10,11,12,30],[230, 300, 350, 500]]
matrix0 = [[1]]
target = 3
target0 = 1
run = Solution()
res =  run.searchMatrix(matrix0,target0)
print (res)