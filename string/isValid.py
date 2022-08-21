# -*- coding:UTF-8 -*-
'''
NC52 括号序列
描述
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

输入："["
返回值：false
'''

class Solution:
    def isValid(self , s ):
        # write code here
        if s is None:
            return False

        s = list(s)
        stack = []

        for i in s:
            if len(stack) == 0:
                stack.append(i)
                continue
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)

        if len(stack) == 0:
            return True

        return False

s = "["
s1= "{[[]]}"

run = Solution()
res =  run.isValid(s1)
print (res)