# -*- coding:UTF-8 -*-
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
给的那个n对括号，写出所有配对括号的组合
For example, given n = 3, a solution set is:
[
"((()))",
"(()())",
"(())()",
"()(())",
"()()()"
]

思路：dfs回溯，设left，right来表示剩余括号数，每当出现一个括号就让left或right减一。
'''


class Solution:
    def generateParenthesis(self, n):
        if n < 1:
            return [""]

        res = []
        self.dfs(n,n,"",res)
        return res


    def dfs(self,left,right,tmp,res):
        if left>right or left<0 or right<0:
            return

        if left == 0 and right == 0:
            res.append(tmp)

        self.dfs(left-1,right,tmp+"(",res)
        self.dfs(left,right-1,tmp+")",res)

n = 3
run = Solution()
res =  run.generateParenthesis(n)
print (res)
