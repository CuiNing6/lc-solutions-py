# -*- coding:UTF-8 -*-
'''
调整数组顺序使奇数位于偶数前面

描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

输入：[1,2,3,4]
返回值：[1,3,2,4]
'''
class Solution:
    def reOrderArray(self , array ):
        # write code here
        odd = []
        even = []

        for i in array:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        res = odd + even

        return res

arr = [1,2,3,4]
run = Solution()
res =  run.reOrderArray(arr)
print (res)