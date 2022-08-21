# -*- coding:UTF-8 -*-
'''
NC103 反转字符串
描述
写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）

示例1
输入："abcd"
返回值："dcba"
'''

class Solution:
    def solve(self , str ):
        # write code here
        if str =="":
            return str
        else:
            return self.solve(str[1:])+str[0]

str = "abcd"
run = Solution()
res =  run.solve(str)
print (res)