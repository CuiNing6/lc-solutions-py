# -*- coding:utf-8 -*-
'''
描述
给定一个长度为n的数组arr，返回arr的最长无重复元素子数组的长度，无重复指的是所有数字都不相同。
子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组

数据范围：0≤arr.length≤10^5，0 < arr[i]≤10^5

示例1
输入：[2,3,4,5]
返回值：4
说明：[2,3,4,5]是最长子数组

示例2
输入：[2,2,3,4,3]
返回值：3
说明：[2,3,4]是最长子数组

示例3
输入：[9]
返回值：1

示例4
输入：[1,2,3,1,2,3,2,2]
返回值：3
说明：最长子数组为[1,2,3]

示例5
输入：[2,2,3,4,8,99,3]
返回值：5
说明：最长子数组为[2,3,4,8,99]
'''

#
#
# @param arr int整型一维数组 the array
# @return int整型
#
class Solution:
    def maxLength(self , arr ):
        # write code here
        if len(arr) == 1:
            return 1

        if len(arr) == 0:
            return 0

        res = 0
        tmp = [arr[0]]

        for i in range(1,len(arr)):
            if arr[i] in tmp:
                res = max(res, len(tmp))
                start = tmp.index(arr[i])
                tmp = tmp[start+1:]
            tmp.append(arr[i])

        return max(res,len(tmp))

arr = [2,2,3,4,3]
run = Solution()
res = run.maxLength(arr)
print(res)