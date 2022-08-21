# -*- coding:UTF-8 -*-
'''
集合的所有子集
描述
现在有一个没有重复元素的整数集合S，求S的所有子集
注意：
你给出的子集中的元素必须按升序排列
给出的解集中不能出现重复的元素

示例
输入：[1,2,3]
返回值：
[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
'''

#
#
# @param A int整型一维数组
# @return int整型二维数组
#
class Solution:
    def subsets(self , A ):
        # write code here
        A1 = set(A)
        A2 = sorted(A1)

        res = [[]]

        for i in A2:
            res = res + [j+[i] for j in res]

        return res

arr = [1,2,3]
run = Solution()
res =  run.subsets(arr)
print (res)