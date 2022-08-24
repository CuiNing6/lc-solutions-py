# -*- coding:utf-8 -*-
'''
描述
给定一个未排序的整数数组nums，请你找出其中没有出现的最小的正整数

进阶： 空间复杂度 O(1)，时间复杂度 O(n)

数据范围:
-2^31<=nums[i]<=2^31-1
0<=len(nums)<=5*10^5

示例1
输入：
[1,0,2]
返回值：3

示例2
输入：[-2,3,4,1,5]
返回值：2

示例3
输入：[4,5,6,8,9]
返回值：1
'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def minNumberDisappeared(self , nums ):
        # write code here
        nums = list(set(nums))
        nums.append(-1)

        i = 0
        while i <= len(nums) - 1:
            if nums[i] > 0 and nums[i] < len(nums):
                a, b = nums[nums[i]], nums[i]
                nums[nums[i]] = b
                nums[i] = a

                if nums[i] == i:
                    i = i + 1
            else:
                i = i + 1


        for j in range(1, len(nums)):
            if nums[j] <= 0 or nums[j] >= len(nums):
                return j

        return len(nums)

nums = [2,1,3,7,6,9,5,11]
run = Solution()
res = run.minNumberDisappeared(nums)
print(res)
