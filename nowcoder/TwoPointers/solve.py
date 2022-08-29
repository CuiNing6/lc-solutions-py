# -*- coding:utf-8 -*-
'''
描述
写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）

数据范围： 0≤n≤1000
要求：空间复杂度 O(n)，时间复杂度 O(n)

示例1
输入："abcd"
返回值："dcba"

示例2
输入：""
返回值：""
'''
#
# 反转字符串
# @param str string字符串
# @return string字符串
#
class Solution:
    def solve(self , str ):
        # write code here
        if len(str) <= 1:
            return str

        n = len(str) - 1
        res = ""
        while n:
            print(str[n])
            res = res + str[n]
            n -= 1

        res = res + str[0]

        return res

str = "abcd"
run =  Solution()
res = run.solve(str)
print(res)
