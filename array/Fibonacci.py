# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1

        res = 1
        tmp = 0

        for i in range(2,n+1):
            res = res + tmp
            tmp = res - tmp

        return res

run = Solution()
res =  run.Fibonacci(6)
print (res)