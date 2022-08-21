# -*- coding:UTF-8 -*-
'''
数组中未出现的最小正整数

描述
给定一个无序数组arr，找到数组中未出现的最小正整数
例如arr = [-1, 2, 3, 4]。返回1
arr = [1, 2, 3, 4]。返回5
[要求]
时间复杂度为O(n)O(n)，空间复杂度为O(1)O(1)

输入：[-1,2,3,4]
返回值：1
'''

class Solution:
    def minNumberdisappered(self , arr ):
        # write code here
        if arr is None:
            return False

        for i in arr:
            if i-1 <= 0:
                continue

            tmp = [i - 1]

            if len(set(arr+tmp)) == len(arr)+1:
                return i-1
            else:
                continue

        return arr[-1]+1

arr = [-1,2,3,4]
arr1 = [1, 2, 3, 4]
run = Solution()
res =  run.minNumberdisappered(arr1)
print (res)