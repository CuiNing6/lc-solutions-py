#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def Fibonacci(self , n ):
        # write code here
        if n == 1 or n == 2:
            return 1

        return self.Fibonacci(n-1) + self.Fibonacci(n-2)

    def Fibonacci_v0(self, n):
        if n == 1 or n == 2:
            return 1

        c, b, a = 2,1,1

        for _ in range(3, n+1):
            c = a + b
            a = b
            b = c

        return c


n = 3
r = Solution()
res = r.Fibonacci_v0(n)
print(res)