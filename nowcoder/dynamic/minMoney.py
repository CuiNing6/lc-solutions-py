#coding:utf-8
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 最少货币数
# @param arr int整型一维数组 the array
# @param aim int整型 the target
# @return int整型
#
class Solution:
    def minMoney(self , arr , aim ):
        # write code here
        if not arr:
            return -1

        if aim == 0:
            return 0

        dp = [aim+1]*(aim+1)
        dp[0] = 0

        for i in range(1,aim+1):
            for j in range(len(arr)):
                if arr[j] <= i:
                    dp[i] = min(dp[i],dp[i-arr[j]]+1)
        if dp[aim] > aim:
            return -1
        else:
            return dp[aim]




arr = [5,2,3]
aim = 20
r = Solution()
res = r.minMoney(arr,aim)
print(res)



