# -*- coding:UTF-8 -*-
'''
max increasing subsequence
数组中的最长连续子序列
描述
给定无序数组arr，返回其中最长的连续序列的长度(要求值连续，位置可以不连续,例如 3,4,5,6为连续的自然数）

示例
输入：[100,4,200,1,3,2]
返回值：4
'''


class Solution:
    def MLS(self , arr ):
        # write code here
        arr_list = set(arr)
        res = {}
        maxlength = 0

        for i in arr_list:
            left = 0
            right = 0

            if i-1 in res:
                left = res[i-1]

            if i+1 in res:
                right = res[i+1]

            length = left + right + 1

            res[i] = length

            res[i-left] = length
            res[i+right] = length

            maxlength = max(length, maxlength)

        return maxlength




arr = [100,4,200,1,3,2]
# arr = [1,1,1]
run = Solution()
res =  run.MLS(arr)
print (res)