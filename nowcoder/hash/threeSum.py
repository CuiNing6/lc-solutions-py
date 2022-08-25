# -*- coding:utf-8 -*-
'''
描述
给出一个有n个元素的数组S，S中是否有元素a,b,c满足a+b+c=0？找出数组S中所有满足条件的三元组。

数据范围：0≤n≤3000，数组中各个元素值满足 |val|≤100
空间复杂度：O(n^2)，时间复杂度 O(n^2)

注意：
三元组（a、b、c）中的元素可以按任意顺序排列。
解集中不能包含重复的三元组。

示例1
输入：[-10,0,10,20,-10,-40]
返回值：[[-10,-10,20],[-10,0,10]]

示例2
输入：[-2,0,1,1,2]
返回值：[[-2,0,2],[-2,1,1]]

示例3
输入：[0,0]
返回值：[]
'''

#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def threeSum(self , num ):
        # write code here
        num = sorted(num)
        res = []

        for first in range(len(num)):
            if first > 0 and num[first] == num[first-1]:
                continue

            third = len(num) - 1
            target = -num[first]

            for second in range(first+1, len(num)):
                if second > first+1 and num[second] == num[second-1]:
                    continue

                while second < third and num[second] + num[third] > target:
                    third -= 1

                if second == third:
                    break

                if num[second] + num[third] == target:
                    res.append([num[first], num[second], num[third]])

        return res

num = [-10,0,10,20,-10,-40]
run = Solution()
res = run.threeSum(num)
print(res)