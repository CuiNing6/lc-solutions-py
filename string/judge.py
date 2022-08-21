# -*- coding:UTF-8 -*-
'''
NC141 判断回文
描述
给定一个字符串，请编写一个函数判断该字符串是否回文。如果回文请返回true，否则返回false。

示例1
输入："absba"

返回值：true
'''

class Solution:
    def judge(self , str ):
        # write code here
        if len(str) == 1:
            return True

        reindex=len(str)
        stindex=0

        for i in range(len(str)//2):
            if str[stindex] == str[reindex-1]:
                reindex -= 1
                stindex += 1
            else:
                return False

        return True

str = "abc1234321ab"
str1= "absba"

run = Solution()
res =  run.judge(str1)
print (res)