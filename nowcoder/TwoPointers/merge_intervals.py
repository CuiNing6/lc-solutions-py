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

class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

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

        intervals = sorted(intervals, key=lambda x: x.start)

        res = [intervals[0]]

        for i in range(1,len(intervals)):
            if res[-1].end >= intervals[i].start and res[-1].end <= intervals[i].end:
                res[-1].end = intervals[i].end
            elif res[-1].end >= intervals[i].end:
                continue
            else:
                res.append(intervals[i])

        return res



#[[2,3],[4,5],[6,7],[8,9],[1,10]]
#[[1,4],[0,2],[3,5]]

# intervals = [Interval(2,3),Interval(4,5),Interval(6,7),Interval(8,9),Interval(1,10)]
intervals = [Interval(1,4),Interval(0,2),Interval(3,5)]
run = Solution()
res = run.merge(intervals)
for i in range(len(res)):
    print(res[i].start, res[i].end)