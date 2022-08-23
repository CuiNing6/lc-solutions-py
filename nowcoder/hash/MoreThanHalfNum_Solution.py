# -*- coding:utf-8 -*-
'''
描述
给一个长度为 n 的数组，数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。

数据范围： n ≤ 50000，数组中元素的值 0≤val≤10000
要求：空间复杂度：O(1)，时间复杂度 O(n)
输入描述：
保证数组输入非空，且保证有解

示例1
输入：[1,2,3,2,2,2,5,4,2]
返回值：2

示例2
输入：[3,3,3,3,2,2,2]
返回值：3

示例3
输入：[1]
返回值：1
'''


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        hash_res = {}

        for i in range(len(numbers)):
            if numbers[i] not in hash_res.keys():
                hash_res[numbers[i]] = 1
            else:
                hash_res[numbers[i]] += 1

        res = list(hash_res.keys())[list(hash_res.values()).index(max(hash_res.values()))]

        return res

numbers = [1,2,3,2,2,2,5,4,2]
run = Solution()
res = run.MoreThanHalfNum_Solution(numbers)
print(res)
