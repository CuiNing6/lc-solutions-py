# -*- coding:utf-8 -*-
'''
描述
一个数组A中存有 n 个整数，在不允许使用另外数组的前提下，将每个整数循环向右移 M（ M >=0）个位置，即将A中的数据由（A0 A1 ……AN-1 ）变换为（AN-M …… AN-1 A0 A1 ……AN-M-1 ）（最后 M 个数循环移至最前面的 M 个位置）。如果需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？

数据范围：0<n≤100，0≤m≤1000
进阶：空间复杂度 O(1)，时间复杂度 O(n)


示例1
输入：6,2,[1,2,3,4,5,6]
返回值：[5,6,1,2,3,4]

示例2
输入：4,0,[1,2,3,4]
返回值：[1,2,3,4]

备注：(1<=N<=100,M>=0)
'''

#
# 旋转数组
# @param n int整型 数组长度
# @param m int整型 右移距离
# @param a int整型一维数组 给定数组
# @return int整型一维数组
#
class Solution:
    def solve(self , n , m , a ):
        # write code here
        if m == n or m == 0:
            return a

        m = m % n

        return a[n-m:] + a[:n-m]

n = 6
m = 2
a = [1,2,3,4,5,6]

run = Solution()
res = run.solve(n, m, a)
print(res)