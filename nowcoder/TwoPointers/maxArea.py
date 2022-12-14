# -*- coding:utf-8 -*-
'''
描述
给定一个数组height，长度为n，每个数代表坐标轴中的一个点的高度，height[i]是在第i点的高度，请问，从中选2个高度与x轴组成的容器最多能容纳多少水
1.你不能倾斜容器
2.当n小于2时，视为不能形成容器，请返回0
3.数据保证能容纳最多的水不会超过整形范围，即不会超过2^31-1

数据范围:0<=height.length<=10^50;0<=height[i]<=10^40

示例1
输入：[1,7,3,2,4,5,8,2,7]
返回值：49

示例2
输入：[2,2]
返回值：2

示例3
输入：[5,4,3,2,1,5]
返回值：25
'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param height int整型一维数组
# @return int整型
#
class Solution:
    def maxArea(self , height ):
        # write code here
        if len(height) < 2:
            return 0

        res = 0
        head = 0
        tail = len(height) - 1
        for i in range(len(height)):
            if tail <= head:
                break
            res = max(res, min(height[head],height[tail])*(tail - head))
            if height[head] < height[tail]:
                head += 1
            else:
                tail -= 1

        return res

height = [6,4,3,1,4,6,99,62,1,2,6]
run = Solution()
res = run.maxArea(height)
print(res)