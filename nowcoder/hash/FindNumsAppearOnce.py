# -*- coding:utf-8 -*-
'''
描述
一个整型数组里除了两个数字只出现一次，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

数据范围：数组长度 2≤n≤1000，数组中每个数的大小 0<val≤1000000
要求：空间复杂度 O(1)，时间复杂度 O(n)

提示：输出时按非降序排列。

示例1
输入：[1,4,1,6]
返回值：[4,6]
说明：
返回的结果中较小的数排在前面

示例2
输入：[1,2,3,3,2,9]
返回值：[1,9]
'''

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self , array ):
        # write code here
        hash_res = {}

        for i in range(len(array)):
            if array[i] not in hash_res.keys():
                hash_res[array[i]] = 1
            else:
                hash_res[array[i]] += 1

        res = [k for k, v in hash_res.items() if v == 1]

        return sorted(res)

array = [1,2,3,3,2,9]
run = Solution()
res = run.FindNumsAppearOnce(array)
print(res)