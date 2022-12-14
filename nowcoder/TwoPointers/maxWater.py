# -*- coding:utf-8 -*-
'''
描述
给定一个整形数组arr，已知其中所有的值都是非负的，将这个数组看作一个柱子高度图，计算按此排列的柱子，下雨之后能接多少雨水。(数组以外的区域高度视为0)
数据范围：数组长度 0≤n≤2×10^5，数组中每个值满足 0<val≤10^9，保证返回结果满足 0≤val≤10^9

要求：时间复杂度 O(n)

示例1
输入：[3,1,2,5,2,4]
返回值：5
说明：数组 [3,1,2,5,2,4] 表示柱子高度图，在这种情况下，可以接 5个单位的雨水，蓝色的为雨水 ，如题面图。

示例2
输入：[4,5,1,3,2]
返回值：2
'''
#
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#
class Solution:
    def maxWater(self , arr ):
        # write code here
        if len(arr) <= 2:
            return 0

        n = len(arr)
        l = 1
        r = n-2
        lmax = arr[0]
        rmax = arr[n-1]

        res = 0

        while l<=r:
            if lmax < rmax:
                if arr[l] < lmax:
                    res += lmax - arr[l]
                else:
                    lmax = arr[l]
                l += 1
            else:
                if arr[r] < rmax:
                    res += rmax - arr[r]
                else:
                    rmax = arr[r]
                r -= 1

        return res


arr = [4,5,1,3,2]
run = Solution()
res = run.maxWater(arr)
print(res)

