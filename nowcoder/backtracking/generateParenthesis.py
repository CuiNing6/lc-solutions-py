#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return string字符串一维数组
#
class Solution:
    def generateParenthesis(self , n ):
        # write code here
        if n == '0':
            return []

        res = []
        right = n
        left = n
        trace = ""

        def dfs(res, trace, left, right):
            if right < left:
                return

            if right < 0 or left < 0:
                return

            if left == 0 and right == 0:
                res.append(trace)

            trace += '('
            dfs(res,trace,left-1,right)
            trace = trace[:-1]

            trace += ')'
            dfs(res,trace,left,right-1)
            trace = trace[:-1]

        dfs(res,trace,left,right)

        return res

n = 3
r = Solution()
res = r.generateParenthesis(n)
print(res)