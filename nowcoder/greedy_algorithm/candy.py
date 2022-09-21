# -*- coding:utf-8 -*-
'''
描述
一群孩子做游戏，现在请你根据游戏得分来发糖果，要求如下：

1. 每个孩子不管得分多少，起码分到一个糖果。
2. 任意两个相邻的孩子之间，得分较多的孩子必须拿多一些糖果。(若相同则无此限制)

给定一个数组 arrarr 代表得分数组，请返回最少需要多少糖果。

要求: 时间复杂度为 O(n)O(n) 空间复杂度为 O(n)O(n)

数据范围： 1≤n≤100000 ，1≤a_i≤1000

示例1
输入：[1,1,2]
返回值：4
说明：最优分配方案为1,1,2

示例2
输入：[1,1,1]
返回值：3
说明：最优分配方案是1,1,1
'''

#
# pick candy
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def candy(self , arr ):
        # write code here
        num = [1] * len(arr)

        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                num[i] = num[i-1] + 1

        res = num[len(arr) - 1]
        j = len(arr) - 2

        while j >= 0:
            if arr[j] > arr[j+1] and num[j] <= num[j+1]:
                num[j] = num[j+1] + 1

            res += num[j]

            j -= 1

        return res

arr = [1,4,2,7,9]
run = Solution()
res = run.candy(arr)
print(res)