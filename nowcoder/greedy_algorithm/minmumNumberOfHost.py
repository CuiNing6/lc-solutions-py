# -*- coding:utf-8 -*-
'''
描述
有 n 个活动即将举办，每个活动都有开始时间与活动的结束时间，第 i 个活动的开始时间是 starti ,第 i 个活动的结束时间是 endi ,举办某个活动就需要为该活动准备一个活动主持人。
一位活动主持人在同一时间只能参与一个活动。并且活动主持人需要全程参与活动，换句话说，一个主持人参与了第 i 个活动，那么该主持人在 (starti,endi) 这个时间段不能参与其他任何活动。求为了成功举办这 n 个活动，最少需要多少名主持人。

数据范围: 1≤n≤10^5， -2^{32}≤start_i≤end_i≤-2^{32}−1

复杂度要求：时间复杂度O(nlogn) ，空间复杂度 O(n)

示例1
输入：2,[[1,2],[2,3]]
返回值：1
说明：只需要一个主持人就能成功举办这两个活动

示例2
输入：2,[[1,3],[2,4]]
返回值：2
说明：需要两个主持人才能成功举办这两个活动

备注：
1≤n≤10^5
start_i,end_istart在int范围内
'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算成功举办活动需要多少名主持人
# @param n int整型 有n个活动
# @param startEnd int整型二维数组 startEnd[i][0]用于表示第i个活动的开始时间，startEnd[i][1]表示第i个活动的结束时间
# @return int整型
#
class Solution:
    def minmumNumberOfHost(self , n , startEnd ):
        # write code here
        res = 0
        start = []
        end = []

        for i in range(n):
            start.append(startEnd[i][0])
            end.append(startEnd[i][1])

        start.sort()
        end.sort()
        j = 0

        for k in range(n):
            if start[k] >= end[j]:
                j += 1
            else:
                res += 1

        return res

n = 2
startEnd = [[1,2],[2,3]]

run = Solution()
res = run.minmumNumberOfHost(n, startEnd)
print(res)