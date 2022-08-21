# -*- coding:UTF-8 -*-
'''
Given a collection of distinct integers, return all possible permutations.
给定不同的整数的集合,返回所有可能的排列。
Input: [1,2,3]
Output:
[
[1,2,3],
[1,3,2],
[2,1,3],
[2,3,1],
[3,1,2],
[3,2,1]
]

思路：O(n2)的方法，如果上面的题会了这道题就算简单题了，47题、77题、78题都是类似的。
'''

class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums,res,[])

        return res

    def dfs(self,nums,res,tmp):
        if not nums:
            res.append(tmp)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:],res,tmp+[nums[i]])

Input = [1,2,3]
run = Solution()
res =  run.permute(Input)
print (res)