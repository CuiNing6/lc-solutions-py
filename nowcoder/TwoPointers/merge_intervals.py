# -*- coding:utf-8 -*-
'''
描述
给出一组区间，请合并所有重叠的区间。
请保证合并后的区间按区间起点升序排列。

数据范围：区间组数 0≤n≤2×10^5，区间内 的值都满足 0≤val≤2×10^5

要求：空间复杂度 O(n)，时间复杂度 O(nlogn)
进阶：空间复杂度 O(val)，时间复杂度O(val)

示例1
输入：[[10,30],[20,60],[80,100],[150,180]]
返回值：[[10,60],[80,100],[150,180]]

示例2
输入：[[0,10],[10,20]]
返回值：[[0,20]]
'''

# class Interval:
#     def __init__(self, a=0, b=0):
#         self.start = a
#         self.end = b

#
#
# @param intervals Interval类一维数组
# @return Interval类一维数组
#
class Solution:
    def merge(self , intervals ):
        # write code here
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0])

        j = 0
        while j < len(intervals) - 1:
            if intervals[j][1] >= intervals[j+1][0]:
                intervals[j][1] = max(intervals[j][1], intervals[j+1][1])
                intervals.remove([intervals[j+1][0],intervals[j+1][1]])
            else:
                j += 1


        return intervals


intervals = [[1,4],[0,2],[3,5]]
run = Solution()
res = run.merge(intervals)
print(res)