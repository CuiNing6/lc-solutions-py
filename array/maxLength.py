# -*- coding:UTF-8 -*-
"""
最长无重复子数组
描述
给定一个数组arr，返回arr的最长无重复元素子数组的长度，无重复指的是所有数字都不相同。
子数组是连续的，比如[1,3,5,7,9]的子数组有[1,3]，[3,5,7]等等，但是[1,3,7]不是子数组

示例
输入：[2,3,4,5]
输出：4
说明：[2,3,4,5]是最长子数组
"""


class Solution:
    def maxLength(self , arr ):
        # write code here
        if len(arr) < 2:
            return len(arr)

        dp = [1 for _ in range(len(arr))]
        d = dict()

        d[arr[0]] = 0

        for i in range(1,len(arr)):
            if arr[i] in d:
                if dp[i-1] >= i - d[arr[i]]:
                    dp[i] = i - d[arr[i]]
                else:
                    dp[i] = dp[i-1] + 1

            else:
                dp[i] = dp[i-1] + 1

            d[arr[i]] = i

        return max(dp)

arr = [2]
run = Solution()
res =  run.maxLength(arr)
print (res)
