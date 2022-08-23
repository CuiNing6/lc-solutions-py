# -*- coding:UTF-8 -*-
'''
描述
给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。
（注：返回的数组下标从1开始算起，保证target一定可以由数组里面2个数字相加得到）

数据范围：2≤len(numbers)≤10^5
 ，-10 ≤numbersi≤10^9
 ，0 ≤target≤10^9

要求：空间复杂度 O(n)，时间复杂度 O(nlogn)

示例1
输入：[3,2,4],6
返回值：[2,3]
说明：
因为 2+4=6 ，而 2的下标为2 ， 4的下标为3 ，又因为 下标2 < 下标3 ，所以返回[2,3]

示例2
输入：[20,70,110,150],90
返回值：[1,2]
说明：20+70=90

@param numbers int整型一维数组
@param target int整型
@return int整型一维数组
'''
class Solution:
    def twoSum(self , numbers , target ):
        # write code here
        hash_res = {}
        res = []

        for i, j in enumerate(numbers):
            if j not in hash_res.keys():
                hash_res[target - j] = i
            else:
                res.extend([hash_res[j]+1, i+1])
                return res

numbers = [3,2,4]
run = Solution()
res = run.twoSum(numbers, 6)
print(res)