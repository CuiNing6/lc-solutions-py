# -*- coding:UTF-8 -*-
'''
三个数的最大乘积
描述
给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1)。

示例
输入：[3,4,1,2]
返回值：24
'''


class Solution:
    def solve(self , A):
        # write code here
        A = sorted(A,reverse=True)
        res0 = A[0]*A[1]*A[2]
        res1 = A[0]*A[-1]*A[-2]

        res = max(res0,res1)

        return res


arr = [1,-5,-2,3]
# arr = [1,1,1]
run = Solution()
res =  run.solve(arr)
print (res)