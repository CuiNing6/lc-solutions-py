# -*- coding:UTF-8 -*-
'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.
给定一些被选中的数字（没有重复的）和一个目标数，找到满足在给定数字序列中和为目标数的集合。数字可以重复使用
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
所有的数都是正整数，不能包含重复的组合。
Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
[7],
[2,2,3]
]
Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
[2,2,2,2],
[2,3,3],
[3,5]
]

思路：该题数组没有排好序，首先得排序。剩下的同样，dfs递归的套路都差不多，用一个辅助函数，每遍历一个数就加入待定的数组tmp，再把目标书target 减去当前遍历过的数。
'''


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        # candidates = sorted(candidates)
        self.dfs(candidates,0,target,res,[])
        return res


    def dfs(self,candidates,index,target,res,tmp):
        if target<0:
            return
        if target == 0:
            res.append(tmp)
            return

        for i in range(index,len(candidates)):
            self.dfs(candidates,i,target-candidates[i],res,tmp+[candidates[i]])


candidates = [2,3,6,7]
target = 7
candidates1 = [2,3,5]
target1 = 8
run = Solution()
res =  run.combinationSum(candidates1,target1)
print (res)










