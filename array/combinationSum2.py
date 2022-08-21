# -*- coding:UTF-8 -*-
'''
加起来和为目标值的组合

描述
给出一组候选数 C 和一个目标数 T，找出候选数中起来和等于 T 的所有组合。
C 中的每个数字在一个组合中只能使用一次。
注意：
题目中所有的数字（包括目标数 T ）都是正整数
组合中的数字 (a_1, a_2, … , a_k) 要按非递增排序 (a_1 < a_2 < … < a_k).
结果中不能包含重复的组合
组合之间的排序按照索引从小到大依次比较，小的排在前面，如果索引相同的情况下数值相同，则比较下一个索引。

输入：[100,10,20,70,60,10,50],80
返回值：[[10,10,60],[10,20,50],[10,70],[20,60]]
说明：给定的候选数集是[100,10,20,70,60,10,50]，目标数是80
'''

class Solution:
    def combinationSum2(self , nums , target):
        # write code here
        if target == 0:
            return [[]]

        if target < 0:
            return []

        nums = sorted(nums)

        res = []
        for i, num in enumerate(nums):
            sub_target = target - num
            sub_res = self.combinationSum2(nums[i+1:], sub_target)
            for i in sub_res:
                if [num]+i in res:
                    continue
                else:
                    res = res + [[num]+i for i in sub_res]

        return res

nums = [100,10,20,70,60,10,50]
target = 80
nums1 = [10,1,2,7,6,1,5]
target1 = 8
run = Solution()
res =  run.combinationSum2(nums , target)
print (res)
