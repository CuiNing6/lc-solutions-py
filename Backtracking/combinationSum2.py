# -*- coding:UTF-8 -*-
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.
给定一些被选中的数字和一个目标数，找到满足在给定数字序列中和为目标数的集合。每个数只能使用一次
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
[1, 7],
[1, 2, 5],
[2, 6],
[1, 1, 6]
]

思路：跟39题非常像，区别在于数组内的数不能重复使用，但数组内可以有重复的数，注意一下相同的数不要遍历两次产生重合的结果就好了
'''


class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates = sorted(candidates)
        self.dfs(candidates,target,res,[])
        return res


    def dfs(self,candidates,target,res,tmp):
        if target<0:
            return
        if target == 0:
            res.append(tmp)
            return

        for i in range(len(candidates)):
            if candidates[i] == candidates[i-1]:
                continue
            self.dfs(candidates[i+1:],target-candidates[i],res,tmp+[candidates[i]])


candidates = [100,10,20,70,60,10,50]
target = 80
candidates1 = [10,1,2,7,6,1,5]
target1 = 8
run = Solution()
res =  run.combinationSum2(candidates,target)
print (res)










